import pandas as pd
import os
import re
from sqlalchemy import create_engine
import json
import numpy as np


def write_df_to_db(df, table):
    engine = create_engine('mysql://root:vaughn@localhost/Texas_Education_Data')
    df.to_sql(table, engine, if_exists='append')

def write_df_to_csv(df, name):
    df.to_csv('./table_csvs/' + name)
    
def get_source_target_mapping(sheet_name):
    data_dict_file = "/Users/jameslinton/Projects/Project_Data/data_schema/Texas Education Data Dictionary.xlsx"
    
    data_dict_df = pd.read_excel(data_dict_file, sheet_name = sheet_name)
    data_dict_df = data_dict_df[['Source Column Name','Column Name']].dropna()
    # data_dict_df = data_dict_df[data_dict_df['Source Column Name']!='Charter Status']

    return dict(zip(data_dict_df['Source Column Name'],data_dict_df['Column Name']))

def get_source_target_mapping_test_scores():
    data_dict_file = "/Users/jameslinton/Projects/Project_Data/data_schema/Texas Education Data Dictionary.xlsx"
    
    data_dict_df = pd.read_excel(data_dict_file, sheet_name = "Test_Scores")
    data_dict_df_1 = data_dict_df[['Source Column Name(2000-2010)', 'Column Name']].dropna()
    data_dict_df_2 = data_dict_df[['Source Column Name(2011-2018)', 'Column Name']].dropna()

    return {"Source Column Name(2000-2010)":dict(zip(data_dict_df_1['Source Column Name(2000-2010)'],data_dict_df_1['Column Name'])),
            "Source Column Name(2011-2018)":dict(zip(data_dict_df_2['Source Column Name(2011-2018)'],data_dict_df_2['Column Name']))}

def get_source_target_mapping_dropout_rates():
    data_dict_file = "/Users/jameslinton/Projects/Project_Data/data_schema/Texas Education Data Dictionary.xlsx"
    
    data_dict_df = pd.read_excel(data_dict_file, sheet_name = "Dropout_Rates")
    data_dict_df_1 = data_dict_df[['Source Column Name(2003-2010)', 'Column Name']].dropna()
    data_dict_df_2 = data_dict_df[['Source Column Name(2011-2013)', 'Column Name']].dropna()
    data_dict_df_3 = data_dict_df[['Source Column Name(2014-2019)', 'Column Name']].dropna()

    return {"Source Column Name(2003-2010)":dict(zip(data_dict_df_1['Source Column Name(2003-2010)'],data_dict_df_1['Column Name'])),
            "Source Column Name(2011-2013)":dict(zip(data_dict_df_2['Source Column Name(2011-2013)'],data_dict_df_2['Column Name'])),
            "Source Column Name(2014-2019)":dict(zip(data_dict_df_3['Source Column Name(2014-2019)'],data_dict_df_3['Column Name']))}

def get_source_target_mapping_classes():
    data_dict_file = "/Users/jameslinton/Projects/Project_Data/data_schema/Texas Education Data Dictionary.xlsx"
    
    data_dict_df = pd.read_excel(data_dict_file, sheet_name = "Classes")
    data_dict_df_1 = data_dict_df[['Source Column Name(2013-2016)', 'Column Name']].dropna()
    data_dict_df_2 = data_dict_df[['Source Column Name(2017-2020)', 'Column Name']].dropna()

    return {"Source Column Name(2013-2016)":dict(zip(data_dict_df_1['Source Column Name(2013-2016)'],data_dict_df_1['Column Name'])),
            "Source Column Name(2017-2020)":dict(zip(data_dict_df_2['Source Column Name(2017-2020)'],data_dict_df_2['Column Name']))}

def normalize_ids(id):
    return int(re.findall('(?!0)[0-9]+', id)[0])

def file_to_df(folder_name, filename, sheet_num=0):
    path = folder_name + filename
    if filename.endswith(".csv"):
        print(path)
        return pd.read_csv(path)
    elif filename.endswith(".xlsx"):
        print(path)
        return pd.read_excel(path, sheet_name=sheet_num)

def folder_to_df(folder_name, year_from_filename=False, sheet_num=0):
    final_df = pd.DataFrame()
    for filename in os.listdir(folder_name):
        if filename.endswith(".csv") or filename.endswith(".xlsx"):
            df = file_to_df(folder_name, filename, sheet_num)
            if year_from_filename:
                year = re.findall('20..',filename)[0]
                df['Year'] = year
            final_df = pd.concat([final_df, df], ignore_index=True)
    
    return final_df

def read_all_files():
    all_files_dict = {}

    #Read financial data
    financial_file_name = "2005-2019-summarized-peims-financial-data.xlsx"
    financial_folder_name = "./data_files/tea_financial_data/"
    financial_df = file_to_df(financial_folder_name, financial_file_name)
    all_files_dict['financial'] = financial_df

    #Read teacher data
    teacher_folder_name = "./data_files/tea_teacher_data/"
    teacher_df = folder_to_df(teacher_folder_name, True)
    all_files_dict['teacher'] = teacher_df

    #Read sat/act data
    test_scores_folder_name_1 = "./data_files/tea_sat_act_data/2000_2010/"
    test_scores_df_1 = folder_to_df(test_scores_folder_name_1, True)

    test_scores_folder_name_2_sat = "./data_files/tea_sat_act_data/2011_2018/sat/"
    test_scores_folder_name_2_act = "./data_files/tea_sat_act_data/2011_2018/act/"
    test_scores_folder_name_2_sat_act = "./data_files/tea_sat_act_data/2011_2018/sat_act/"
    
    test_scores_df_2_sat = folder_to_df(test_scores_folder_name_2_sat, True)
    test_scores_df_2_act = folder_to_df(test_scores_folder_name_2_act, True)
    test_scores_df_2_sat_act = folder_to_df(test_scores_folder_name_2_sat_act, True)

    all_files_dict['test_scores'] = [test_scores_df_1, [test_scores_df_2_sat, test_scores_df_2_act, test_scores_df_2_sat_act]]

    #Read graduation data
    graduation_folder_name_1 = "./data_files/tea_graduation_data/2003_2010/"
    graduation_folder_name_2 = "./data_files/tea_graduation_data/2011_2013/"
    graduation_folder_name_3 = "./data_files/tea_graduation_data/2014_2019/"

    graduation_df_1 = folder_to_df(graduation_folder_name_1, True)
    graduation_df_2 = folder_to_df(graduation_folder_name_2, True)
    graduation_df_3 = folder_to_df(graduation_folder_name_3, True, 2)

    all_files_dict['graduation'] = [graduation_df_1, graduation_df_2, graduation_df_3]
    
    #Read classes data
    classes_folder_name_1 = "./data_files/tea_class_data/2013_2016/"
    classes_folder_name_2 = "./data_files/tea_class_data/2017_2020/"

    classes_df_1 = folder_to_df(classes_folder_name_1)
    classes_df_2 = folder_to_df(classes_folder_name_2)

    all_files_dict['classes'] = [classes_df_1, classes_df_2]

    return all_files_dict

def get_districts_df(all_files_dict):
    #Get column name maps for teacher data and financial data
    districts_dict = get_source_target_mapping("Districts")
    teacher_dict = dict(list(districts_dict.items())[2:])
    financial_dict = dict(list(districts_dict.items())[:2])
    
    #Get Charter_Flag column from teacher data
    teacher_df = all_files_dict['teacher']
    charter_df = teacher_df[teacher_dict.keys()].rename(columns=teacher_dict)
    charter_df['Charter_Flag'] = charter_df['Charter_Flag'].apply(lambda c: 1 if c == 'OPEN ENROLLMENT CHARTER' else 0)

    #Get District_Id and District_Name columns from financial data
    financial_df = all_files_dict['financial']
    districts_df = financial_df[financial_dict.keys()].rename(columns=financial_dict).set_index('District_Id')

    #Combine columns with multiple names into one name
    districts_df = districts_df.drop_duplicates().groupby(['District_Id'])['District_Name'].apply(lambda x: ", ".join(x)).reset_index()
    
    #Convert Id strings into numbers
    districts_df['District_Id'] = districts_df['District_Id'].apply(normalize_ids)
    districts_df = districts_df.set_index('District_Id')

    #Append charter column
    districts_df = districts_df.join(charter_df)

    return districts_df

def get_revenue_df(all_files_dict):
    revenue_dict = get_source_target_mapping("Revenue")

    #Get revenue columns from financial data
    financial_df = all_files_dict['financial']
    revenue_df = financial_df[revenue_dict.keys()].rename(columns=revenue_dict)
    
    #Convert Id strings into numbers
    revenue_df['District_Id'] = revenue_df['District_Id'].apply(normalize_ids)
    revenue_df = revenue_df.set_index('District_Id')

    return revenue_df

def get_program_df(all_files_dict):
    program_dict = get_source_target_mapping("Programs")

    #Get program columns from financial data
    financial_df = all_files_dict['financial']
    program_df = financial_df[program_dict.keys()].rename(columns=program_dict)
    
    #Convert Id strings into numbers
    program_df['District_Id'] = program_df['District_Id'].apply(normalize_ids)
    program_df = program_df.set_index('District_Id')

    return program_df

def get_function_df(all_files_dict):
    function_dict = get_source_target_mapping("Functions")

    #Get function columns from financial data
    financial_df = all_files_dict['financial']
    function_df = financial_df[function_dict.keys()].rename(columns=function_dict)
    
    #Convert Id strings into numbers
    function_df['District_Id'] = function_df['District_Id'].apply(normalize_ids)
    function_df = function_df.set_index('District_Id')

    return function_df

def get_teacher_df(all_files_dict, district_df):
    #Get teacher column mapping
    teacher_dict = get_source_target_mapping("Teachers")
    teacher_dict.pop('from file name')
    teacher_dict['Year'] = 'Year'

    #Get teacher columns from teacher data
    teacher_df = all_files_dict['teacher']
    teacher_df = teacher_df[teacher_dict.keys()].rename(columns=teacher_dict)
    teacher_df = teacher_df.set_index('District_Id')

    #Map each staff category to a number
    staff_category_map = {}
    for i,category in enumerate(teacher_df['Staff_Category'].unique()):
        staff_category_map[category]=i

    with open('./db_dicts/Staff_Category_Dict.json', 'w') as file:
        file.write(json.dumps(staff_category_map))
    
    teacher_df['Staff_Category'] = teacher_df['Staff_Category'].map(staff_category_map)

    #Map each staff area to a number
    staff_area_map = {}
    for i,area in enumerate(teacher_df['Staff_Area'].unique()):
        staff_area_map[area]=i

    with open('./db_dicts/Staff_Area_Dict.json', 'w') as file:
        file.write(json.dumps(staff_area_map))

    teacher_df['Staff_Area'] = teacher_df['Staff_Area'].map(staff_area_map)

    #Remove '.' values
    teacher_df=teacher_df.drop(teacher_df[(teacher_df['Num_Employees'] == '.')|(teacher_df['Total_Employee_Pay'] == '.')|(teacher_df['Avg_Pay'] == '.')].index)
    
    #Remove district ids not in financial data
    final_test_scores_df = normalize_districts(teacher_df, district_df)

    return teacher_df

def get_test_scores_df(all_files_dict, district_df):
    test_scores_dict_1 = get_source_target_mapping_test_scores()['Source Column Name(2000-2010)']

    test_scores_df_1 = all_files_dict['test_scores'][0]#2000-2010 data

    #Clean DISTRICT field to be ints
    test_scores_df_1['DISTRICT'] = test_scores_df_1['DISTRICT'].replace('^=\"0*|\"$','',regex=True).astype('int')
    test_scores_df_1 = test_scores_df_1.set_index('DISTRICT')

    #Create final empty df
    # final_test_scores_df_1 = pd.DataFrame(columns=(list(test_scores_dict_1.values()) + ['DISTRICT','Year'])).set_index(['DISTRICT','Year'])
    final_test_scores_df_1 = pd.DataFrame(columns=['DISTRICT','Year']).set_index(['DISTRICT','Year'])
    #Loop through target columns
    for regex,target_name in test_scores_dict_1.items():
        #Get columns that match regex to combine
        curr_col_df = test_scores_df_1.filter(regex=regex).assign(Year=test_scores_df_1['Year']).reset_index().set_index(['DISTRICT','Year'])
        
        tmp_target_col = pd.DataFrame(columns=['DISTRICT','Year',target_name]).set_index(['DISTRICT','Year'])[target_name]
        for col in curr_col_df.columns:
            tmp_target_col = tmp_target_col.append(curr_col_df[col].dropna())
        
        final_test_scores_df_1 = pd.concat([final_test_scores_df_1,tmp_target_col.rename(target_name).to_frame()],axis=1)

    final_test_scores_df_1 = final_test_scores_df_1.reset_index().rename(columns={'DISTRICT':'District_Id'}).set_index(['District_Id','Year'])

    #Remove -1 and . values
    for col_name in final_test_scores_df_1.columns:
        final_test_scores_df_1[col_name] = final_test_scores_df_1[col_name].replace('-1',np.nan).replace('.',np.nan)

    #Put SAT data into 1 df
    test_scores_df_2_sat = all_files_dict['test_scores'][1][0]
    test_scores_df_2_sat = test_scores_df_2_sat[test_scores_df_2_sat['Group']=='All Students']
    test_scores_df_2_sat = normalize_district_column(test_scores_df_2_sat,'_Sat')

    #Put ACT data into 1 df
    test_scores_df_2_act = all_files_dict['test_scores'][1][1]
    test_scores_df_2_act = test_scores_df_2_act[test_scores_df_2_act['Group']=='All Students']
    test_scores_df_2_act = normalize_district_column(test_scores_df_2_act,'_Act')

    #Put SAT and ACT data into 1 df
    test_scores_df_2_sat_act = all_files_dict['test_scores'][1][2]
    test_scores_df_2_sat_act = test_scores_df_2_sat_act[test_scores_df_2_sat_act['Group']=='All Students']
    test_scores_df_2_sat_act = normalize_district_column(test_scores_df_2_sat_act,'_Sat_Act')

    #Put ACT,SAT, and SAT ACT data into 1 df
    test_scores_df_2 = pd.concat([test_scores_df_2_sat_act,test_scores_df_2_act,test_scores_df_2_sat],axis=1)
    
    #Rename columns
    test_scores_dict_2 = get_source_target_mapping_test_scores()['Source Column Name(2011-2018)']
    del test_scores_dict_2['Will be gotten from file name']
    del test_scores_dict_2['District']
    test_scores_df_2 = test_scores_df_2[test_scores_dict_2.keys()].rename(columns=test_scores_dict_2)

    #Remove < form rows and remove ="num" from rows as well
    for col_name in test_scores_df_2.columns:
        if 'Total' in col_name or 'Num' in col_name:
            test_scores_df_2[col_name] = test_scores_df_2[col_name].replace('^=\"|\"$|,','',regex=True).replace('^<.*',np.nan,regex=True).astype('float').astype('Int64')
        else:
            test_scores_df_2[col_name] = test_scores_df_2[col_name].replace('^=\"|\"$|,','',regex=True).replace('^<.*',np.nan,regex=True).astype('float')

    #Combine df_1 and df_2
    test_scores_df = pd.concat([final_test_scores_df_1, test_scores_df_2]).reset_index().set_index(['District_Id','Year']).sort_index().dropna(how='all')

    #Remove districts not in financial data
    final_test_scores_df = normalize_districts(test_scores_df, district_df)

    return final_test_scores_df

def normalize_district_column(df,col_postfix=''):
    district_values = ['DISTRICT','District']
    tmp_df_list = []

    for value in district_values:
        tmp_df = df[~df[value].isnull()].drop(columns=[x for x in district_values if x!=value])
        tmp_df[value] = tmp_df[value].replace('^=\"0*|\"$','',regex=True).astype('int')
        tmp_df = tmp_df.rename(columns={value:'District_Id'}).set_index(['District_Id','Year'])
        tmp_df_list.append(tmp_df)
        
    
    return pd.concat(tmp_df_list).rename(lambda x: x + col_postfix, axis='columns')

def get_dropout_rates_df(all_files_dict, district_df):
    dropout_rates_df_1 = all_files_dict['graduation'][0]
    dropout_rates_df_2 = all_files_dict['graduation'][1]
    dropout_rates_df_3 = all_files_dict['graduation'][2]

    dropout_rates_dict = get_source_target_mapping_dropout_rates()

    #Clean and normalize data from 2003-2010
    dropout_rates_df_1 = dropout_rates_df_1[dropout_rates_df_1['Gradespan'] == 912]
    dropout_rates_dict_1 = dropout_rates_dict['Source Column Name(2003-2010)']
    del dropout_rates_dict_1['Will be gotten from file name']
    dropout_rates_df_1 = dropout_rates_df_1[list(dropout_rates_dict_1.keys()) + ['Year']].rename(columns=dropout_rates_dict_1).set_index(['District_Id','Year'])
    for col_name in dropout_rates_df_1.columns:
        dropout_rates_df_1[col_name] = dropout_rates_df_1[col_name].replace('<','',regex=True).replace('^-$|^\.$',np.nan,regex=True).astype('float')

    #Clean and normalize data from 2011-2013
    dropout_rates_df_2 = dropout_rates_df_2[dropout_rates_df_2['Gradespan'] == 912]
    dropout_rates_df_2['CALC_PER_TEC'] = dropout_rates_df_2[['CALC_PER_TEC_39053', 'CALC_PER_TEC']].replace(np.nan,'').apply(lambda x:''.join(x),axis=1)
    dropout_rates_df_2 = dropout_rates_df_2[dropout_rates_df_2['CALC_PER_TEC'] == 'Yes']
    dropout_rates_dict_2 = dropout_rates_dict['Source Column Name(2011-2013)']
    del dropout_rates_dict_2['Will be gotten from file name']
    dropout_rates_df_2 = dropout_rates_df_2[list(dropout_rates_dict_2.keys()) + ['Year']].rename(columns=dropout_rates_dict_2).set_index(['District_Id','Year'])
    for col_name in dropout_rates_df_2.columns:
        dropout_rates_df_2[col_name] = dropout_rates_df_2[col_name].replace('<','',regex=True).replace('^-$|^\.$',np.nan,regex=True).astype('float')

    #Clean and normalize data from 2014-2019
    dropout_rates_df_3['Gradespan'] = dropout_rates_df_3[['Gradespan','GRADESPAN']].replace(np.nan,0).sum(axis=1)
    dropout_rates_df_3 = dropout_rates_df_3[(dropout_rates_df_3['Gradespan'] == 912) & (dropout_rates_df_3['CALC_FOR_STATE_ACCT'] == 'Yes')]
    dropout_rates_dict_3 = dropout_rates_dict['Source Column Name(2014-2019)']
    del dropout_rates_dict_3['Will be gotten from file name']
    dropout_rates_df_3 = dropout_rates_df_3[list(dropout_rates_dict_3.keys()) + ['Year']].rename(columns=dropout_rates_dict_3).set_index(['District_Id','Year'])
    for col_name in dropout_rates_df_3.columns:
        dropout_rates_df_3[col_name] = dropout_rates_df_3[col_name].replace('<','',regex=True).replace('^-$|^\.$',np.nan,regex=True).astype('float')

    #Combine into 1 df
    dropout_rates_df = pd.concat([dropout_rates_df_1, dropout_rates_df_2, dropout_rates_df_3]).sort_index()

    #Remove districts not in financial data
    final_dropout_rates_df = normalize_districts(dropout_rates_df, district_df)

    return final_dropout_rates_df

def normalize_districts(new_df, district_df):
    new_df_index = list(new_df.index.names)
    district_set = set(district_df.index)
    new_set = set(new_df.reset_index().set_index('District_Id').index)
    diff_set = new_set.difference(district_set)
    new_df = new_df.reset_index().set_index('District_Id').drop(list(diff_set))
    new_df = new_df.reset_index().set_index(new_df_index)

    return new_df

def get_classes_df(all_files_dict, district_df):
    classes_df_1 = all_files_dict['classes'][0]
    classes_df_2 = all_files_dict['classes'][1]

    classes_dict = get_source_target_mapping_classes()

    classes_dict_1 = classes_dict['Source Column Name(2013-2016)']
    classes_dict_2 = classes_dict['Source Column Name(2017-2020)']

    classes_df_1 = classes_df_1[classes_dict_1.keys()].rename(columns=classes_dict_1)
    classes_df_2 = classes_df_2[classes_dict_2.keys()].rename(columns=classes_dict_2)

    classes_df_1['Year'] = classes_df_1['Year'].replace('^20[0-9]{2}-','',regex=True)
    classes_df_2['Year'] = classes_df_2['Year'].replace('^20[0-9]{2}-','',regex=True)

    classes_df_1['Num_Students'] = classes_df_1['Num_Students'].apply(lambda x: np.nan if x < 0 else x)
    classes_df_2['Num_Students'] = classes_df_2['Num_Students'].apply(lambda x: np.nan if x < 0 else x)

    classes_df_1 = classes_df_1.loc[classes_df_1[['Num_Teachers', 'Num_Students']].dropna(how='all').index]
    classes_df_2 = classes_df_2.loc[classes_df_2[['Num_Teachers', 'Num_Students']].dropna(how='all').index]

    classes_df_1  = classes_df_1.set_index(['District_Id','Year','Subject','Grade_Level'])
    classes_df_2  = classes_df_2.set_index(['District_Id','Year','Subject','Grade_Level'])

    classes_df = pd.concat([classes_df_1, classes_df_2]).reset_index()

    subject_map = {}
    for i,category in enumerate(classes_df['Subject'].unique()):
        subject_map[category]=i

    with open('./db_dicts/Subject_Dict.json', 'w') as file:
        file.write(json.dumps(subject_map))

    classes_df['Subject'] = classes_df['Subject'].map(subject_map)

    grade_level_map= {}
    for i,category in enumerate(classes_df['Grade_Level'].unique()):
        grade_level_map[category]=i

    with open('./db_dicts/Grade_Level_Dict.json', 'w') as file:
        file.write(json.dumps(grade_level_map))

    classes_df['Grade_Level'] = classes_df['Grade_Level'].map(grade_level_map)

    classes_df['Num_Teachers'] = classes_df['Num_Teachers'].replace('.',np.nan).astype('float')

    classes_df = classes_df.groupby(['District_Id','Year','Subject', 'Grade_Level']).sum().sort_index()

    final_classes_df = normalize_districts(classes_df, district_df)

    return final_classes_df

def get_enrollment_df(all_files_dict):
    financial_df = all_files_dict['financial']
    enrollment_df = financial_df[['DISTRICT NUMBER','YEAR','FALL SURVEY ENROLLMENT']]

    enrollment_dict = get_source_target_mapping("Enrollment")
    enrollment_df = enrollment_df.rename(columns=enrollment_dict)

    enrollment_df['District_Id'] = enrollment_df['District_Id'].apply(normalize_ids)
    enrollment_df = enrollment_df.set_index(['District_Id','Year'])

    return enrollment_df

all_files_dict = read_all_files()
# district_df = get_districts_df(all_files_dict)
# revenue_df = get_revenue_df(all_files_dict)
# program_df = get_program_df(all_files_dict)
# function_df = get_function_df(all_files_dict)
# teacher_df = get_teacher_df(all_files_dict, district_df)
# test_scores_df = get_test_scores_df(all_files_dict,district_df)
# dropout_rates_df = get_dropout_rates_df(all_files_dict, district_df)
# classes_df = get_classes_df(all_files_dict, district_df)
enrollment_df = get_enrollment_df(all_files_dict)