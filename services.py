#type of province
province_1 = ['An Giang', 'Bắc Giang', 'Bạc Liêu', 'Bắc Ninh', 'Bến Tre',
       'Bình Định', 'Bình Dương', 'Bình Phước', 'Cần Thơ', 'Đắk Lắk',
       'Đắk Nông', 'Đồng Nai', 'Đồng Tháp', 'Gia Lai', 'Hà Nam',
       'Hà Tĩnh', 'Hải Dương', 'Hải Phòng', 'Hậu Giang', 'Hoà Bình',
       'Kon Tum', 'Long An', 'Nam Định', 'Ninh Bình', 'Ninh Thuận',
       'Phú Thọ', 'Phú Yên', 'Sóc Trăng', 'Sơn La', 'Tây Ninh',
       'Thái Bình', 'Thái Nguyên', 'Tiền Giang', 'Trà Vinh', 'Vĩnh Long',
       'Vĩnh Phúc']

province_2 = ['Bà Rịa - Vũng Tàu', 'Bắc Kạn', 'Bình Thuận', 'Cà Mau', 'Cao Bằng',
       'Đà Nẵng', 'Hà Giang', 'Hà Nội', 'Hồ Chí Minh', 'Hưng Yên',
       'Khánh Hòa', 'Lai Châu', 'Lâm Đồng', 'Lạng Sơn', 'Lào Cai',
       'Nghệ An', 'Quảng Bình', 'Quảng Nam', 'Quảng Ninh', 'Quảng Trị',
       'Thanh Hóa', 'Thừa Thiên Huế', 'Tuyên Quang', 'Yên Bái']

province_3 = ['Điện Biên', 'Kiên Giang', 'Quảng Ngãi']

#lanes
intra_metro = ['HCM-HCM', 'HCM-HCM2', 'HN-HN', 'HN-HN2']

cross_metro = ['HCM-HN', 'HCM-HN2', 'HN-HCM', 'HN-HCM2']

cross_region = ['HCM-North', 'HCM-North1', 'HCM-North2', 'HCM-North3', 'HCM-North4', 'HCM-NorthHY', 'HCM-NorthVI', 'HN-South1',
                'HN-South2', 'HN-South4', 'HN-SouthNTR', 'HN-SouthTN','HN-SouthVIL', 'North-HCM', 'North-HCM2', 'NorthHY-HCM',
                'NorthHY-HCM2', 'NorthHY-South1', 'NorthHY-South2','NorthHY-South4', 'NorthHY-SouthNTR', 'NorthHY-SouthTN',
                'NorthHY-SouthVIL', 'North-South1', 'North-South2', 'North-South4','North-SouthNTR', 'North-SouthTN', 'North-SouthVIL', 'South-HN',
                'South-HN2', 'South-North', 'South-North1', 'South-North2','South-North3', 'South-North4', 'South-NorthHY', 'South-NorthVI',
                'SouthNTR-HN', 'SouthNTR-HN2', 'SouthNTR-North', 'SouthNTR-North1','SouthNTR-North2', 'SouthNTR-North3', 'SouthNTR-North4',
                'SouthNTR-NorthHY', 'SouthNTR-NorthVI', 'SouthTN-HN','SouthTN-HN2', 'SouthTN-North1', 'SouthTN-North2',
                'SouthTN-North3', 'SouthTN-North4', 'SouthTN-NorthHY','SouthTN-NorthVI', 'SouthVIL-HN', 'SouthVIL-HN2', 'SouthVIL-North',
                'SouthVIL-North1', 'SouthVIL-North2', 'SouthVIL-North3','SouthVIL-North4', 'SouthVIL-NorthHY', 'SouthVIL-NorthVI',
                'SouthTN-North']

same_region = ['Central-Central', 'Central-Central1', 'Central-Central2','HCM-South1', 'HCM-South2', 'HCM-South4', 'HCM-SouthNTR',
                'HCM-SouthTN', 'HCM-SouthVIL', 'HN-North', 'HN-North1','HN-North2', 'HN-North3', 'HN-North4', 'HN-NorthHY', 'HN-NorthVI',
                'North-HN', 'North-HN2', 'NorthHY-HN', 'NorthHY-HN2','NorthHY-North', 'NorthHY-North1', 'NorthHY-North2',
                'NorthHY-North3', 'NorthHY-North4', 'NorthHY-NorthHY','NorthHY-NorthVI', 'North-North', 'North-North1', 'North-North2',
                'North-North3', 'North-North4', 'North-NorthHY', 'North-NorthVI','South-HCM', 'South-HCM2', 'SouthNTR-HCM', 'SouthNTR-HCM2',
                'SouthNTR-South1', 'SouthNTR-South2', 'SouthNTR-South4','SouthNTR-SouthNTR', 'SouthNTR-SouthTN', 'SouthNTR-SouthVIL',
                'South-South1', 'South-South2', 'South-South4', 'South-SouthNTR','South-SouthTN', 'South-SouthVIL', 'SouthTN-HCM', 'SouthTN-HCM2',
                'SouthTN-South1', 'SouthTN-South2', 'SouthTN-South4','SouthTN-SouthNTR', 'SouthTN-SouthTN', 'SouthTN-SouthVIL',
                'SouthVIL-HCM', 'SouthVIL-HCM2', 'SouthVIL-South1','SouthVIL-South2', 'SouthVIL-South4', 'SouthVIL-SouthNTR',
                'SouthVIL-SouthTN', 'SouthVIL-SouthVIL']

cross_central = ['Central-HCM', 'Central-HCM2', 'Central-HN', 'Central-HN2','Central-North', 'Central-North1', 'Central-North2',
                'Central-North3', 'Central-North4', 'Central-NorthHY','Central-NorthVI', 'Central-South1', 'Central-South2',
                'Central-South4', 'Central-SouthNTR', 'Central-SouthTN','Central-SouthVIL', 'HCM-Central', 'HCM-Central1', 'HCM-Central2',
                'HN-Central', 'HN-Central1', 'HN-Central2', 'North-Central','North-Central1', 'North-Central2', 'NorthHY-Central',
                'NorthHY-Central1', 'NorthHY-Central2', 'South-Central','South-Central1', 'South-Central2', 'SouthNTR-Central1',
                'SouthNTR-Central2', 'SouthTN-Central', 'SouthTN-Central1','SouthTN-Central2', 'SouthVIL-Central1', 'SouthVIL-Central2']