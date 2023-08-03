import ond
# check origin province of type 1
def check_serivce_o1(o_province):
    origin_north = ['Bắc Giang','Bắc Ninh','Hà Nam','Hà Tĩnh','Hoà Bình','Ninh Bình','Phú Thọ','Sơn La','Thái Nguyên','Vĩnh Phúc']
    origin_northHY = ['Hải Dương','Hải Phòng','Nam Định','Thái Bình']
    origin_south = ['An Giang','Bình Dương','Bình Phước','Đồng Nai','Long An','Tây Ninh']
    origin_southNTR = ['Bình Định','Ninh Thuận','Phú Yên']
    origin_southTN = ['Đắk Lắk','Đắk Nông','Gia Lai','Kon Tum']
    origin_southVIL = ['Bạc Liêu','Bến Tre','Cần Thơ','Đồng Tháp','Hậu Giang','Sóc Trăng','Tiền Giang','Trà Vinh','Vĩnh Long']

    if o_province in origin_north:
        return 'North'
    
    elif o_province in origin_northHY:
        return 'NorthHY'

    elif o_province in origin_south:
        return 'South'
    
    elif o_province in origin_southNTR:
        return 'SouthNTR'
    
    elif o_province in origin_southTN:
        return 'SouthTN'
    
    elif o_province in origin_southVIL:
        return 'SouthVIL'
    
# check destination province of type 1 
def check_service_d1(d_province):
    dest_north1 = ['Bắc Giang','Bắc Ninh','Hà Nam','Hoà Bình','Ninh Bình','Phú Thọ','Thái Nguyên','Vĩnh Phúc']
    dest_north2 = 'Sơn La'
    dest_northHY = ['Hải Dương','Hải Phòng','Nam Định','Thái Bình']
    dest_northVI = 'Hà Tĩnh'
    dest_south1 = ['An Giang','Bình Dương','Bình Phước','Đồng Nai','Long An','Tây Ninh']
    dest_southVIL = ['Bạc Liêu','Bến Tre','Cần Thơ','Đồng Tháp','Hậu Giang','Sóc Trăng','Tiền Giang','Trà Vinh','Vĩnh Long']
    dest_southTN = ['Đắk Lắk','Đắk Nông','Gia Lai','Kon Tum']
    dest_southNTR = ['Bình Định','Ninh Thuận','Phú Yên']

    if d_province in dest_north1:
        return 'North1'
    
    elif d_province in dest_north2:
        return 'North2'

    elif d_province in dest_northHY:
        return 'NorthHY'
    
    elif d_province in dest_northVI:
        return 'NorthVI'
    
    elif d_province in dest_south1:
        return 'South1'
    
    elif d_province in dest_southVIL:
        return 'SouthVIL'
    
    elif d_province in dest_southTN:
        return 'SouthTN'
    
    elif d_province in dest_southNTR:
        return 'SouthNTR'
    
# check origin province of type 2
def check_service_o2(o_province, filter_2_o_central = ond.filter_2_o_central, filter_2_o_hcm = ond.filter_2_o_hcm,
                    filter_2_o_hn = ond.filter_2_o_hn, filter_2_o_north = ond.filter_2_o_north, filter_2_o_northHY = ond.filter_2_o_northHY,
                    filter_2_o_south = ond.filter_2_o_south, filter_2_o_southNTR = ond.filter_2_o_southNTR):
    
    if o_province in filter_2_o_central:
        return 'Central'

    elif o_province in filter_2_o_hcm:
        return 'HCM'
    
    elif o_province in filter_2_o_hn:
        return 'HN'
    
    elif o_province in filter_2_o_north:
        return 'North'
    
    elif o_province in filter_2_o_northHY:
        return 'NorthHY'
    
    elif o_province in filter_2_o_south:
        return 'South'

    elif o_province in filter_2_o_southNTR:
        return 'SouthNTR'

# check destination province of type 2    
def check_service_d2(d_province, filter_2_d_central=ond.filter_2_d_central, filter_2_d_central1=ond.filter_2_d_central1,
                     filter_2_d_central2=ond.filter_2_d_central2, filter_2_d_hcm=ond.filter_2_d_hcm,filter_2_d_hcm2=ond.filter_2_d_hcm2,
                     filter_2_d_hn=ond.filter_2_d_hn, filter_2_d_hn2=ond.filter_2_d_hn2,filter_2_d_north=ond.filter_2_d_north,
                     filter_2_d_north1=ond.filter_2_d_north1,filter_2_d_north2=ond.filter_2_d_north2,
                     filter_2_d_north3=ond.filter_2_d_north3,filter_2_d_north4=ond.filter_2_d_north4,
                     filter_2_d_northHY=ond.filter_2_d_northHY,filter_2_d_northVI=ond.filter_2_d_northVI,
                     filter_2_d_south1=ond.filter_2_d_south1,filter_2_d_south2=ond.filter_2_d_south2,
                     filter_2_d_south4=ond.filter_2_d_south4,filter_2_d_southNTR=ond.filter_2_d_southNTR):

    if d_province in filter_2_d_central:
        return 'Central'
    
    elif d_province in filter_2_d_central1:
        return 'Central1'

    elif d_province in filter_2_d_central2:
        return 'Central2'
    
    elif d_province in filter_2_d_hcm:
        return 'HCM'
    
    elif d_province in filter_2_d_hcm2:
        return 'HCM2'
    
    elif d_province in filter_2_d_hn:
        return 'HN'
    
    elif d_province in filter_2_d_hn2:
        return 'HN2'
    
    elif d_province in filter_2_d_north:
        return 'North'
    
    elif d_province in filter_2_d_north1:
        return 'North1'
    
    elif d_province in filter_2_d_north2:
        return 'North2'
    
    elif d_province in filter_2_d_north3:
        return 'Norht3'
    
    elif d_province in filter_2_d_north4:
        return 'North4'
    
    elif d_province in filter_2_d_northHY:
        return 'NorthHY'
    
    elif d_province in filter_2_d_northVI:
        return 'NorthVI'
    
    elif d_province in filter_2_d_south1:
        return 'South1'
    
    elif d_province in filter_2_d_south2:
        return 'South2'
    
    elif d_province in filter_2_d_south4:
        return 'South4'
    
    elif d_province in filter_2_d_southNTR:
        return 'SouthNTR'
    
# check origin province of type 3
def check_service_o3(o_province, filter_3_o_central=ond.filter_3_o_central, filter_3_o_north=ond.filter_3_o_north,
                     filter_3_o_south=ond.filter_3_o_south):

    #origin

    if o_province in filter_3_o_central:
        return 'Central'
    
    elif o_province in filter_3_o_north:
        return 'North'
    
    elif o_province in filter_3_o_south:
        return 'South'
    

# check destination province of type 3   
def check_service_d3(d_province, filter_3_d_central1=ond.filter_3_d_central1, filter_3_d_central2=ond.filter_3_d_central2,
                     filter_3_d_north1=ond.filter_3_d_north1,filter_3_d_north2=ond.filter_3_d_north2,
                     filter_3_d_north3=ond.filter_3_d_north3,filter_3_d_south1=ond.filter_3_d_south1,
                     filter_3_d_south2=ond.filter_3_d_south2,filter_3_d_south4=ond.filter_3_d_south4):

    if d_province in filter_3_d_central1:
        return 'Central1'
    
    if d_province in filter_3_d_central2:
        return 'Central2'
    
    if d_province in filter_3_d_north1:
        return 'North1'
    
    if d_province in filter_3_d_north2:
        return 'North2'
    
    if d_province in filter_3_d_north3:
        return 'North3'
    
    if d_province in filter_3_d_south1:
        return 'South1'
    
    if d_province in filter_3_d_south2:
        return 'South2'
    
    if d_province in filter_3_d_south4:
        return 'South4'
    
