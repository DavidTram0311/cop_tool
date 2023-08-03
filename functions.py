import filters
import services 
import pandas as pd

def filter_ond(province):
    if province in services.province_1:
        return 1
    elif province in services.province_2:
        return 2
    elif province in services.province_3:
        return 3
    
def region_o(province, district, services):
    if services == 1:
        return filters.check_serivce_o1(province)

    elif services == 2:
        return filters.check_service_o2(province + district)

    elif services == 3:
        return filters.check_service_o3(province + district)

def region_d(province, district, services):
    if services == 1:
        return filters.check_service_d1(province)

    if services == 2:
        return filters.check_service_d2(province + district)

    if services == 3:
        return filters.check_service_d3(province + district)

def lanes(origin, dest):
    return origin + '-' + dest

def routes(lanes):
    if lanes in services.intra_metro:
        return 'Intra metro'
    
    if lanes in services.cross_metro:
        return 'Cross metro'
    
    if lanes in services.cross_region:
        return 'Cross region'
    
    if lanes in services.same_region:
        return 'Same region'
    
    if lanes in services.cross_central:
        return 'Cross central'
    
def week_of_year(date):
    if date:
        return date.week
    else:
        return 0

def leadtime(start,end):
    if int(str(start - end)[0:2]) < 0:
        return 0
    else:
        return (int(str(start - end)[0:2]) * 24) + (pd.Timedelta(start - end).seconds / 3600.0)
    
def month_of_year(date):
    if date:
        return date.month
    else:
        return 0
    
def success_rate(actual, rts, completed_w_m, rts_w_m, summary_actual, summary_rts):
    third_pls = []
    w_m = []
    success_rate = []
    for i in range(len(actual)):
        for j in range(len(rts)):
            if actual['Transporter'][i] == rts['Transporter'][j] and actual[completed_w_m][i] == rts[rts_w_m][j]:
                third_pls.append(actual['Transporter'][i])
                w_m.append(actual[completed_w_m][i])
                actual_order = actual[summary_actual][i]
                rts_order = rts[summary_rts][j]
                rate = (actual_order/(actual_order+rts_order)) * 100
                success_rate.append(rate)

    summary = pd.DataFrame(list(zip(third_pls,w_m,success_rate)),
                             columns=['3pls','week/month','success_rate'])
    
    return summary

def leadtime_actual(leadtime_lanes, orders_lanes, actual_deli_m_w, actual, route_region):
    third_pls = []
    routes_region = []
    m_w = []
    leadtime = []
    for i in range(len(leadtime_lanes)):
        for j in range(len(orders_lanes)):
            if leadtime_lanes['Transporter'][i] == orders_lanes['Transporter'][j] and leadtime_lanes[route_region][i] == orders_lanes[route_region][j] and leadtime_lanes[actual_deli_m_w][i] == orders_lanes[actual_deli_m_w][j]:
                third_pls.append(leadtime_lanes['Transporter'][i])
                routes_region.append(leadtime_lanes[route_region][i])
                m_w.append(leadtime_lanes[actual_deli_m_w][i])

                hours = leadtime_lanes['leadtime'][i]/orders_lanes[actual][j]
                leadtime.append(hours)

    leadtimes = pd.DataFrame(list(zip(third_pls,routes_region,m_w,leadtime)),
                             columns=['3pls','routes/regions','week/month','leadtime(hours)'])
    
    return leadtimes


# Update on GGsheet

# Monthly and Weekly Successrate

def update_values_wn_sr(sh, week_lst, summary_weekly, title):
  third_pls = ['GHTK','GHN','J&T','NJV','Best']
  # if 1 week
  if len(week_lst) == 1:
    summary_w = summary_weekly[summary_weekly['week/month'] == float(week_lst[0])]

    worksheet = sh.add_worksheet(title=title, rows=100, cols=20)

    worksheet.update('B1', week_lst[0])

    num = 1
    # for i in range(len(summary_w['3pls'])):
    #   num = num + 1
    #   cell1 = 'A' + str(num)
    #   cell2 = 'B' + str(num)

    #   worksheet.update(cell1, summary_w.iloc[i,0])
    #   worksheet.update(cell2, summary_w.iloc[i,2])

    for i in range(len(third_pls)): # 1 = GHTK
       for j in range(len(summary_w)):          
          if third_pls[i] == 'GHTK' and summary_w.iloc[j,0] == 'GiaoHangTietKiem': # i = 1 (GHTK), j = 4
            num = num + 1
            cell1 = 'A' + str(num)
            cell2 = 'B' + str(num)
            worksheet.update(cell1, third_pls[i])
            worksheet.update(cell2, summary_w.iloc[j,2])
          
          elif third_pls[i] == 'GHN' and summary_w.iloc[j,0] == 'GiaoHangNhanhV2':
            num = num + 1
            cell1 = 'A' + str(num)
            cell2 = 'B' + str(num)
            worksheet.update(cell1, third_pls[i])
            worksheet.update(cell2, summary_w.iloc[j,2])
             
          elif third_pls[i] == 'J&T' and summary_w.iloc[j,0] == 'JNT':
            num = num + 1
            cell1 = 'A' + str(num)
            cell2 = 'B' + str(num)
            worksheet.update(cell1, third_pls[i])
            worksheet.update(cell2, summary_w.iloc[j,2])
            
          elif third_pls[i] == 'NJV' and summary_w.iloc[j,0] == 'NJV':
            num = num + 1
            cell1 = 'A' + str(num)
            cell2 = 'B' + str(num)
            worksheet.update(cell1, third_pls[i])
            worksheet.update(cell2, summary_w.iloc[j,2])          

          elif third_pls[i] == 'Best' and summary_w.iloc[j,0] == 'BestExpress':
            num = num + 1
            cell1 = 'A' + str(num)
            cell2 = 'B' + str(num)
            worksheet.update(cell1, third_pls[i])
            worksheet.update(cell2, summary_w.iloc[j,2])
             

  # If 2 week
  elif len(week_lst) == 2:
    summary_w = summary_weekly[summary_weekly['week/month'].isin([float(week_lst[0]),float(week_lst[1])])]

    worksheet = sh.add_worksheet(title=title, rows=100, cols=20)

    text = ['B', 'C']

    for i in range(len(week_lst)):
      cell = text[i] + '1'
      worksheet.update(cell, week_lst[i])

    num = 1
    num1 = 1
    num2 = 1
    for i in range(len(summary_w['3pls'].unique())):
      num = num + 1
      cell1 = 'A' + str(num)
      worksheet.update(cell1, summary_w['3pls'].unique()[i])
      
      for j in range(len(summary_w)):

          if summary_w.iloc[j,1] == float(week_lst[0]) and summary_w.iloc[j,0] == summary_w['3pls'].unique()[i]:
            num1 = num1+1
            cell2 = text[0] + str(num1)
            worksheet.update(cell2, summary_w.iloc[j,2])
          
          elif summary_w.iloc[j,1] == float(week_lst[1]) and summary_w.iloc[j,0] == summary_w['3pls'].unique()[i]:
            num2 = num2 + 1
            cell3 = text[1] + str(num2)
            worksheet.update(cell3, summary_w.iloc[j,2])
          
         

    # num1 = 1
    # num2 = 1
    # for i in range(len(summary_w)):

    #   if summary_w.iloc[i,1] == float(week_lst[0]):
    #     num1 = num1 + 1
    #     cell2 = text[0] + str(num1)
    #     worksheet.update(cell2, summary_w.iloc[i,2])
    #   else:
    #     num2 = num2 + 1
    #     cell3 = text[1] + str(num2)
    #     worksheet.update(cell3, summary_w.iloc[i,2])



# Monthly and weekly leadtime

# Format 1
def leadtime_update(worksheet, leadtime_m, month_lst, x, y, route): # x = 2, 9, 16, 23, 30
  third_pls = ['GHTK','GHN','J&T','NJV','Best']
  if len(month_lst) == 1:
    n1 = x
    worksheet.update('A' + str(x), route) #A2, 9,16,23,30. Update route
    worksheet.update('B' + str(x), month_lst[0]) #B2 month
    # for i in range(len(leadtime_m['3pls'].unique())):
    #   n1 = n1 + 1
    #   worksheet.update('A' + str(n1), leadtime_m['3pls'].unique()[i])
    
    for i in range(len(third_pls)):
       for j in range(len(leadtime_m)):
          if third_pls[i] == 'GHTK' and leadtime_m.iloc[j,0] == 'GiaoHangTietKiem' and leadtime_m.iloc[j,1] == route:
            n1 = n1 + 1
            worksheet.update('A' + str(n1), third_pls[i])
            worksheet.update('B' + str(n1), leadtime_m.iloc[j,3])
             
            worksheet.update('E' + str(y), third_pls[i])
            worksheet.update('F' + str(y), leadtime_m.iloc[j,1])
            worksheet.update('G' + str(y), leadtime_m.iloc[j,3])

          elif third_pls[i] == 'GHN' and leadtime_m.iloc[j,0] == 'GiaoHangNhanhV2' and leadtime_m.iloc[j,1] == route:
            n1 = n1 + 1
            worksheet.update('A' + str(n1), third_pls[i])
            worksheet.update('B' + str(n1), leadtime_m.iloc[j,3])

            worksheet.update('E' + str(y+5), third_pls[i])
            worksheet.update('F' + str(y+5), leadtime_m.iloc[j,1])
            worksheet.update('G' + str(y+5), leadtime_m.iloc[j,3])

          elif third_pls[i] == 'J&T' and leadtime_m.iloc[j,0] == 'JNT' and leadtime_m.iloc[j,1] == route:
            n1 = n1 + 1
            worksheet.update('A' + str(n1), third_pls[i])
            worksheet.update('B' + str(n1), leadtime_m.iloc[j,3])

            worksheet.update('E' + str(y+10), third_pls[i])
            worksheet.update('F' + str(y+10), leadtime_m.iloc[j,1])
            worksheet.update('G' + str(y+10), leadtime_m.iloc[j,3])

          elif third_pls[i] == 'NJV' and leadtime_m.iloc[j,0] == 'NJV' and leadtime_m.iloc[j,1] == route:
            n1 = n1 + 1
            worksheet.update('A' + str(n1), third_pls[i])
            worksheet.update('B' + str(n1), leadtime_m.iloc[j,3])

            worksheet.update('E' + str(y+15), third_pls[i])
            worksheet.update('F' + str(y+15), leadtime_m.iloc[j,1])
            worksheet.update('G' + str(y+15), leadtime_m.iloc[j,3])

          elif third_pls[i] == 'Best' and leadtime_m.iloc[j,0] == 'BestExpress' and leadtime_m.iloc[j,1] == route:
            n1 = n1 + 1
            worksheet.update('A' + str(n1), third_pls[i])
            worksheet.update('B' + str(n1), leadtime_m.iloc[j,3])

            worksheet.update('E' + str(y+20), third_pls[i])     
            worksheet.update('F' + str(y+20), leadtime_m.iloc[j,1])
            worksheet.update('G' + str(y+20), leadtime_m.iloc[j,3])


    # n2 = x 
    # for i in range(len(leadtime_m)):

    #   if leadtime_m.iloc[i,1] == route:
    #     n2 = n2 + 1
    #     worksheet.update('B' + str(n2), leadtime_m.iloc[i,3])
    
  elif len(month_lst) == 2:
    n1 = x
    worksheet.update('A' + str(x), route)
    worksheet.update('B' + str(x), month_lst[0])
    worksheet.update('C' + str(x), month_lst[1])


    for i in range(len(leadtime_m['3pls'].unique())):
      n1 = n1 + 1
      worksheet.update('A' + str(n1), leadtime_m['3pls'].unique()[i])

    n2 = x
    n3 = x
    for i in range(len(leadtime_m)):
      if leadtime_m.iloc[i,1] == route:
        if leadtime_m.iloc[i,2] == month_lst[0]:
          n2 = n2 + 1
          worksheet.update('B' + str(n2), leadtime_m.iloc[i,3])
        
        else:
          n3 = n3 + 1
          worksheet.update('C' + str(n3), leadtime_m.iloc[i,3])


# By route
def leadtime_gsheet_route(sh, month_lst, leadtime_month, title, time):
    
  if len(month_lst) == 1:
    leadtime_m = leadtime_month[leadtime_month['week/month'] == float(month_lst[0])]
    worksheet = sh.add_worksheet(title=title, rows=100, cols=20)
    worksheet.update('A1', time)

    # Format 1
    leadtime_update(worksheet, leadtime_m, month_lst, 2, 3, 'Intra metro')

    leadtime_update(worksheet, leadtime_m, month_lst, 9, 4, 'Cross metro')

    leadtime_update(worksheet, leadtime_m, month_lst, 16, 5, 'Cross region')

    leadtime_update(worksheet, leadtime_m, month_lst, 23, 6, 'Same region')

    leadtime_update(worksheet, leadtime_m, month_lst, 30, 7, 'Cross central')


  elif len(month_lst) == 2:
    leadtime_m = leadtime_month[leadtime_month['week/month'].isin([float(month_lst[0]), float(month_lst[1])])]
    worksheet = sh.add_worksheet(title=title, rows=100, cols=20)
    worksheet.update('A1', time)

    leadtime_update(worksheet, leadtime_m, month_lst, 2, 'Intra metro')

    leadtime_update(worksheet, leadtime_m, month_lst, 9, 'Cross metro')

    leadtime_update(worksheet, leadtime_m, month_lst, 16, 'Cross region')

    leadtime_update(worksheet, leadtime_m, month_lst, 23, 'Same region')

    leadtime_update(worksheet, leadtime_m, month_lst, 30, 'Cross central')





            
        