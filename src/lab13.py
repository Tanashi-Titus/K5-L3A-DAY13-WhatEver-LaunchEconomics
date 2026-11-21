"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import NormalIndPower

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000  # đồng / tháng
KHOI_LUONG_THANG = 45_000     # yêu cầu / tháng ở quy mô đầy đủ


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1.0 / p
    return (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs)

    return dict(
        token=float(tien_token.sum()),
        tool=float(tien_tool.sum()),
        chay_lai=float(chay_lai),
        xem_lai=float(xem_lai),
        lam_lai=float(lam_lai),
        tong=float(tong),
        thanh_cong=thanh_cong,
        cps=float(tong / thanh_cong),
        hoa_don_moi_yc=float(hoa_don_moi_yc),
    )


# ---------- Nhiệm vụ D1 · Cỡ mẫu so hai tỉ lệ ----------
def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ bằng công thức chuẩn z."""
    za = NormalDist().inv_cdf(1.0 - alpha / 2.0)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2.0
    n = (
        za * math.sqrt(2.0 * pb * (1.0 - pb))
        + zb * math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2))
    ) ** 2 / (p2 - p1) ** 2
    return math.ceil(n)


def in_cp1(runs, reqs):
    """In kết quả Nhiệm vụ A1, A2, A3, A4."""
    print('\n=== CP1 · NHIỆM VỤ A1: BA PHÉP THỬ ĐÁP ÁN BIẾT TRƯỚC ===')
    kiem_tra_dap_an_biet_truoc()
    print(f'  E[số lần chạy](p=0.8, k=2)   = {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  E[số lần chạy](p=0.8, k=∞)   = {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  Hệ số chi phí (p=0.8, k=3)   = {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    print('\n=== CP1 · NHIỆM VỤ A2: MÔ HÌNH CHI PHÍ TỪ TRACE ===')
    ket_qua = mo_hinh(runs, reqs)
    nhan_map = {
        'token': 'đo từ trace',
        'tool': 'đo từ trace',
        'chay_lai': 'đo từ trace',
        'xem_lai': 'simulated',
        'lam_lai': 'simulated',
        'tong': 'có phần simulated',
        'thanh_cong': '',
        'cps': 'simulated',
        'hoa_don_moi_yc': 'đo từ trace',
    }
    for ten, gia_tri in ket_qua.items():
        fmt = f'{gia_tri:>14,.1f}' if ten == 'hoa_don_moi_yc' else f'{gia_tri:>14,.0f}'
        print(f'  {ten:15s} {fmt}   {nhan_map[ten]}')

    ti_le_gap = ket_qua['cps'] / ket_qua['hoa_don_moi_yc']
    pct_lam_lai = ket_qua['lam_lai'] / ket_qua['tong'] * 100
    pct_xem_lai = ket_qua['xem_lai'] / ket_qua['tong'] * 100
    pct_nhan_vien = (ket_qua['xem_lai'] + ket_qua['lam_lai']) / ket_qua['tong'] * 100
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    ca_he_thong_moi_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'  Số phút xem lại [simulated] : {reqs["phut_xem_lai_simulated"].sum():,.0f} phút')
    print(f'  Số phút làm lại [simulated] : {reqs["phut_lam_lai_simulated"].sum():,.0f} phút')
    print(f'  Tổng số lần gọi tool        : {runs["tool_calls"].sum():,.0f}')
    print(f'  CPS / hoá đơn mỗi yêu cầu   : {ti_le_gap:.1f}× [simulated]')
    print(f'  Tỉ trọng làm lại / xem lại  : {pct_lam_lai:.1f}% / {pct_xem_lai:.1f}% (giờ NV: {pct_nhan_vien:.1f}%) [simulated]')
    print(f'  Chi phí cả hệ thống / yc    : {ca_he_thong_moi_yc:,.0f} đ ({ca_he_thong_moi_yc / BASELINE:.2f}× của 12.000 đ) [simulated]')

    print('\n=== CP1 · NHIỆM VỤ A3: TÁCH THEO LOẠI YÊU CẦU ===')
    print(f'  {"Loại":10s} {"Số yc":>6s} {"Thành công":>11s} {"Lần/yc":>8s} {"CPS [sim]":>12s} {"So 12k":>8s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub_reqs = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub_reqs)
        ti_le_tc = kq['thanh_cong'] / len(sub_reqs) * 100
        lan_tb = sub_reqs['so_lan_chay'].mean()
        print(
            f'  {loai:10s} {len(sub_reqs):>6d} {ti_le_tc:>10.1f}% '
            f'{lan_tb:>8.2f} {kq["cps"]:>11,.0f}đ {kq["cps"] / BASELINE:>7.2f}×'
        )

    print('\n  Tỉ lệ status == "ok" theo loại và lần thử (attempt):')
    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['is_ok'] = (runs_loai['status'] == 'ok').astype(float)
    pivot_ok = runs_loai.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    pivot_ok = pivot_ok.reindex(['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'])
    for loai, row in pivot_ok.iterrows():
        cols = '  '.join(f'Lần {int(a)}: {val:5.1f}%' for a, val in row.items())
        print(f'    {loai:10s} -> {cols}')

    print('\n=== CP1 · NHIỆM VỤ A4: CHI PHÍ CỐ ĐỊNH (noi_dia + hang_nang) ===')
    reqs_pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, reqs_pv)
    print(f'  Phạm vi noi_dia + hang_nang : {len(reqs_pv)} yc, {kq_pv["thanh_cong"]} thành công, '
          f'tổng {kq_pv["tong"]:,.0f} đ, CPS = {kq_pv["cps"]:,.0f} đ [simulated]')
    for nhan_kl, khoi_luong in [('45.000 yc/tháng', KHOI_LUONG_THANG), ('Một nửa (22.500 yc/tháng)', KHOI_LUONG_THANG / 2)]:
        viec_thang = khoi_luong * (kq_pv['thanh_cong'] / len(reqs))
        co_dinh_moi_viec = CHI_PHI_CO_DINH / viec_thang
        cps_co_dinh = kq_pv['cps'] + co_dinh_moi_viec
        print(
            f'  {nhan_kl:26s} -> {viec_thang:>7,.0f} việc/tháng | '
            f'cố định {co_dinh_moi_viec:>5,.0f} đ | '
            f'CPS + cố định = {cps_co_dinh:>6,.0f} đ ({cps_co_dinh / BASELINE:.2f}×) [simulated]'
        )
    return ket_qua


def in_cp2(runs, reqs, goc):
    """In kết quả Nhiệm vụ B1, B2, B3, B4."""
    print('\n=== CP2 · NHIỆM VỤ B1: BẢNG ĐỘ NHẠY (ĐỔI TỪNG YẾU TỐ) [simulated] ===')
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':    dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm nửa':   dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':    dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm nửa':   dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':       dict(max_lan_chay=1),
    }
    ket_qua_b1 = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps / goc - 1.0) * 100.0
        ket_qua_b1[ten] = (cps, pct)
        print(f'  {ten:28s} {cps:>9,.0f} đ  ({pct:+6.1f}%)')

    # Tự kiểm tra tuyến tính: giảm nửa == -0.5 * tăng gấp đôi
    for k_tang, k_giam in [
        ('Giá token gấp đôi', 'Giá token giảm một nửa'),
        ('Tỉ lệ xem lại gấp đôi', 'Tỉ lệ xem lại giảm nửa'),
        ('Số ca làm lại gấp đôi', 'Số ca làm lại giảm nửa'),
    ]:
        assert abs(ket_qua_b1[k_giam][1] + 0.5 * ket_qua_b1[k_tang][1]) < 1e-9
    print('  Tự kiểm tra giảm nửa = -1/2 mức tăng gấp đôi: ĐẠT')

    print('\n=== CP2 · NHIỆM VỤ B2: ĐỔI MỘT CẶP VÀ XẾP HẠNG [simulated] ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    pct_cap = (cps_cap / goc - 1.0) * 100.0
    print(f'  Token ×2 + Xem lại ×2      : {cps_cap:,.0f} đ ({pct_cap:+.1f}%)')
    print(f'  Tổng hai tác động riêng    : {ket_qua_b1["Giá token gấp đôi"][1] + ket_qua_b1["Tỉ lệ xem lại gấp đôi"][1]:+.1f}% (cộng tuyến tính)')

    yeu_to_xep_hang = [
        ('Số ca làm lại (×2)', abs(ket_qua_b1['Số ca làm lại gấp đôi'][1])),
        ('Tỉ lệ xem lại (×2)', abs(ket_qua_b1['Tỉ lệ xem lại gấp đôi'][1])),
        ('Lương nhân viên (+25%)', abs(ket_qua_b1['Lương nhân viên tăng 25%'][1])),
        ('Giới hạn chạy (1 lần)', abs(ket_qua_b1['Chỉ cho chạy 1 lần'][1])),
        ('Giá token (×2)', abs(ket_qua_b1['Giá token gấp đôi'][1])),
    ]
    yeu_to_xep_hang.sort(key=lambda x: x[1], reverse=True)
    top3 = ' · '.join(f'{i}. {ten} ({val:.1f}%)' for i, (ten, val) in enumerate(yeu_to_xep_hang[:3], 1))
    print(f'  Top 3 yếu tố nhạy nhất     : {top3}')

    print('\n=== CP2 · NHIỆM VỤ B3: GIỚI HẠN CHẠY LẠI VÀ CHI PHÍ CẢ HỆ THỐNG [simulated] ===')
    print(f'  {"Giới hạn":10s} {"Tổng trợ lý":>14s} {"Không TC":>10s} {"Cả hệ thống":>14s} {"CPS [sim]":>12s}')
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        he_thong = kq['tong'] + khong_tc * BASELINE
        print(f'  {f"{k} lần":10s} {kq["tong"]:>13,.0f}đ {khong_tc:>10d} {he_thong:>13,.0f}đ {kq["cps"]:>11,.0f}đ')

    print('\n=== CP2 · NHIỆM VỤ B4: XEM LẠI 100% (noi_dia + hang_nang) [simulated] ===')
    reqs_pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(reqs_pv['request_id'])]
    kq_pv = mo_hinh(runs, reqs_pv)

    yc_co_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((reqs_pv['ket_qua'] == 'lam_lai').sum())
    token_tool_pv = kq_pv['token'] + kq_pv['tool']
    tc_pv = kq_pv['thanh_cong']
    xem_lai_100 = yc_co_ok * 5 * LUONG_PHUT

    # Theo đề bài: 9 phút / ca làm lại
    lam_lai_9 = so_lam_lai * 9 * LUONG_PHUT
    tong_9 = token_tool_pv + xem_lai_100 + lam_lai_9
    cps_9 = tong_9 / tc_pv
    hoa_von_9 = (BASELINE * tc_pv - token_tool_pv - lam_lai_9) / (yc_co_ok * LUONG_PHUT)

    # Theo dữ liệu thực tế cột phut_lam_lai_simulated trên các ca lam_lai
    tb_phut_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    tv_phut_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].median()
    lam_lai_tt = so_lam_lai * tb_phut_lam_lai * LUONG_PHUT
    tong_tt = token_tool_pv + xem_lai_100 + lam_lai_tt
    cps_tt = tong_tt / tc_pv
    hoa_von_tt = (BASELINE * tc_pv - token_tool_pv - lam_lai_tt) / (yc_co_ok * LUONG_PHUT)

    print(f'  Phạm vi noi_dia + hang_nang: {len(reqs_pv)} yc, {yc_co_ok} yc có run ok, {so_lam_lai} ca lam_lai, {tc_pv} thành công')
    print(f'  Token + tool               : {token_tool_pv:,.0f} đ | Xem lại 100% (5 phút): {xem_lai_100:,.0f} đ [simulated]')
    print(f'  Với 9 phút/ca làm lại      : tổng {tong_9:,.0f} đ -> CPS = {cps_9:,.0f} đ ({cps_9 / BASELINE:.2f}×) | hoà vốn ≤ {hoa_von_9:.1f} phút/lần xem lại [simulated]')
    print(f'  Với {tb_phut_lam_lai:.1f} phút (TB dữ liệu, TV {tv_phut_lam_lai:.1f}): tổng {tong_tt:,.0f} đ -> CPS = {cps_tt:,.0f} đ ({cps_tt / BASELINE:.2f}×) | hoà vốn ≤ {hoa_von_tt:.1f} phút/lần xem lại [simulated]')


def in_cp4_va_e1(reqs):
    """In kết quả Nhiệm vụ D1 (cỡ mẫu), tỉ lệ an toàn hiện tại (D3) và ba chỉ số chạy thử (E1)."""
    print('\n=== CP4 · NHIỆM VỤ D1: CỠ MẪU PILOT (p1=0.70, alpha=0.05, power=0.80, ICC=0.02) ===')
    p1, alpha, power, icc = 0.70, 0.05, 0.80, 0.02

    # a) Chia theo yêu cầu (MDE +5 điểm)
    n_5pp = co_mau_hai_ti_le(p1, 0.75, alpha, power)
    n_5pp_sm = math.ceil(
        NormalIndPower().solve_power(
            effect_size=proportion_effectsize(0.75, p1),
            power=power,
            alpha=alpha,
            ratio=1.0,
            alternative='two-sided',
        )
    )
    print(f'  a) Theo yêu cầu (+5 điểm)  : {n_5pp:,d} yc/nhóm (statsmodels Cohen h: {n_5pp_sm:,d})')

    # b) Chia theo nhân viên, m = 75
    m_b = 75
    de_b = 1.0 + (m_b - 1) * icc
    n_b = math.ceil(n_5pp * de_b)
    so_nv_nhom = math.ceil(n_b / m_b)
    print(f'  b) Theo nhân viên (m=75)   : DE = {de_b:.2f} -> {n_b:,d} yc/nhóm -> {so_nv_nhom} NV/nhóm (tổng {so_nv_nhom * 2} > 40: KHÔNG ĐỦ)')

    # c) 20 nhân viên mỗi nhóm
    max_eff_nv = 20 / icc
    print(f'  c) 20 nhân viên / nhóm     : cỡ mẫu hiệu dụng tối đa < c/ICC = {max_eff_nv:,.0f} < {n_5pp:,d} (KHÔNG ĐẠT 5 điểm)')

    # d) 6 depot mỗi nhóm
    max_eff_depot = 6 / icc
    print(f'  d) 6 depot / nhóm          : cỡ mẫu hiệu dụng tối đa < c/ICC = {max_eff_depot:,.0f} < {n_5pp:,d} (KHÔNG ĐẠT)')

    # e) MDE +6 điểm, 20 nhân viên mỗi nhóm
    n_6pp = co_mau_hai_ti_le(p1, 0.76, alpha, power)
    # 20*m / (1 + (m - 1)*icc) >= n_6pp  =>  m*(20 - n_6pp*icc) >= n_6pp*(1 - icc)
    m_min = math.ceil(n_6pp * (1.0 - icc) / (20.0 - n_6pp * icc))
    de_e = 1.0 + (m_min - 1) * icc
    power_at_5pp = NormalIndPower().power(
        effect_size=proportion_effectsize(0.75, p1),
        nobs1=n_6pp,
        alpha=alpha,
        ratio=1.0,
        alternative='two-sided',
    )
    print(f'  e) MDE +6 điểm (20 NV/nhóm): n_hiệu_dụng = {n_6pp:,d}/nhóm -> cần m ≥ {m_min} yc/NV (DE = {de_e:.2f})')
    print(f'     Đánh đổi: nếu tác động thật là +5 điểm ở n={n_6pp}, power chỉ còn {power_at_5pp:.2f}')

    # D3: Tỉ lệ mở lại hiện tại trước khi đặt luật dừng an toàn
    ti_le_mo_lai = reqs['mo_lai_trong_7_ngay'].mean() * 100
    so_mo_lai = int(reqs['mo_lai_trong_7_ngay'].sum())
    reqs_pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    ti_le_mo_lai_pv = reqs_pv['mo_lai_trong_7_ngay'].mean() * 100
    print(f'  D3 · mo_lai_trong_7_ngay   : toàn mẫu = {ti_le_mo_lai:.2f}% ({so_mo_lai}/{len(reqs)}) | '
          f'noi_dia+hang_nang = {ti_le_mo_lai_pv:.2f}% ({int(reqs_pv["mo_lai_trong_7_ngay"].sum())}/{len(reqs_pv)})')

    print('\n=== CP5 · NHIỆM VỤ E1: BA CHỈ SỐ TÍNH THỬ TRÊN 1.200 YÊU CẦU ===')
    chinh_mask = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua_mask = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    an_toan_mask = reqs['mo_lai_trong_7_ngay'] == 1
    print(f'  Chính (đóng 24h & không mở lại 7 ngày): {chinh_mask.mean() * 100:.2f}% ({int(chinh_mask.sum())}/{len(reqs)})')
    print(f'  Dùng  (tỉ lệ bỏ qua gợi ý: sua + bo)  : {bo_qua_mask.mean() * 100:.2f}% ({int(bo_qua_mask.sum())}/{len(xem)})')
    print(f'  An toàn (mở lại trong 7 ngày)         : {an_toan_mask.mean() * 100:.2f}% ({int(an_toan_mask.sum())}/{len(reqs)})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    ket_qua_a2 = in_cp1(runs, reqs)
    in_cp2(runs, reqs, ket_qua_a2['cps'])
    in_cp4_va_e1(reqs)
