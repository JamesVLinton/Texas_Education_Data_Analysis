CREATE TABLE `Districts` (
  `District_Id` int PRIMARY KEY,
  `District_Name` varchar(255),
  `Charter_Flag` boolean
);

CREATE TABLE `Enrollment` (
  `District_Id` int,
  `Year` int,
  `Fall_Enrollment` int,
  PRIMARY KEY (`District_Id`, `Year`)
);

CREATE TABLE `Classes` (
  `District_Id` int,
  `Year` int,
  `Subject` int,
  `Grade_Level` int,
  `Num_Teachers` decimal(30,20),
  `Num_Students` decimal(30,20),
  `Class_Size` decimal(30,20),
  `Class_Size_Per_Grade` decimal(30,20),
  `Class_Size_Per_Subject` decimal(30,20),
  PRIMARY KEY (`District_Id`, `Year`, `Subject`, `Grade_Level`)
);

CREATE TABLE`Teachers` (
  `District_Id` int,
  `Year` int,
  `Staff_Category` int,
  `Staff_Area` int,
  `Num_Employees` decimal(10,5),
  `Total_Employee_Pay` int,
  `Avg_Pay` int,
  `Avg_Salary` int,
  `Avg_Salary_Administration` int,
  `Avg_Salary_Teachers` int,
  PRIMARY KEY (`District_Id`, `Year`, `Staff_Category`, `Staff_Area`)
);

CREATE TABLE `Revenue` (
  `District_Id` int,
  `Year` int,
  `Total_Revenue_All_Funds` bigint,
  `Total_Revenue_General_Funds` bigint,
  `Total_Federal_Revenue_All_Funds` bigint,
  `Total_Federal_Revenue_General_Funds` bigint,
  `Total_State_Revenue_All_Funds` bigint,
  `Total_State_Revenue_General_Funds` bigint,
  `Total_Local_Revenue_All_Funds` bigint,
  `Total_Local_Revenue_General_Funds` bigint,
  PRIMARY KEY (`District_Id`, `Year`)
);

CREATE TABLE `Programs` (
  `District_Id` int,
  `Year` int,
  `Regular_All_Funds` int,
  `Regular_General_Funds` int,
  `Gifted_Talented_All_Funds` int,
  `Gifted_Talented_General_Funds` int,
  `Career_Technology_All_Funds` int,
  `Career_Technology_General_Funds` int,
  `Students_With_Disabilities_All_Funds` int,
  `Students_With_Disabilities_General_Funds` int,
  `Compensatory_Education_All_Funds` int,
  `Compensatory_Education_General_Funds` int,
  `Bilingual_All_Funds` int,
  `Bilingual_General_Funds` int,
  `Athletics_Related_Activities_All_Funds` int,
  `Athletics_Related_Activities_General_Funds` int,
  `High_School_Allotment_All_Funds` int,
  `High_School_Allotment_General_Funds` int,
  `Pre_K_Regular_All_Funds` int,
  `Pre_K_Regular_General_Funds` int,
  `Pre_K_Bilingual_All_Funds` int,
  `Pre_K_Bilingual_General_Funds` int,
  `Pre_K_Comp_Ed_All_Funds` int,
  `Pre_K_Comp_Ed_General_Funds` int,
  `Pre_K_Total_All_Funds` int,
  `Pre_K_Total_General_Funds` int,
  `Total_Program_Expenditures_All_Funds` int,
  `Total_Program_Expenditures_General_Funds` int,
  PRIMARY KEY (`District_Id`, `Year`)
);

CREATE TABLE `Functions` (
  `District_Id` int,
  `Year` int,
  `Instruction_All_Funds` int,
  `Instruction_General_Funds` int,
  `Instructional_Res_Media_All_Funds` int,
  `Instructional_Res_Media_General_Funds` int,
  `Curriculum_Staff_Develop_All_Funds` int,
  `Curriculum_Staff_Develop_General_Funds` int,
  `Instructional_Leadership_All_Funds` int,
  `Instructional_Leadership_General_Funds` int,
  `School_Administration_All_Funds` int,
  `School_Administration_General_Funds` int,
  `Guidance_Counseling_Services_All_Funds` int,
  `Guidance_Counseling_Services_General_Funds` int,
  `Social_Work_Services_All_Funds` int,
  `Social_Work_Services_General_Funds` int,
  `Health_Services_All_Funds` int,
  `Health_Services_General_Funds` int,
  `Transportation_All_Funds` int,
  `Transportation_General_Funds` int,
  `Food_All_Funds` int,
  `Food_General_Funds` int,
  `Cocurricular_All_Funds` int,
  `Cocurricular_General_Funds` int,
  `General_Administration_All_Funds` int,
  `General_Administration_General_Funds` int,
  `Plant_Maintenance_Operation_All_Funds` int,
  `Plant_Maintenance_Operation_General_Funds` int,
  `Security_Monitoring_All_Funds` int,
  `Security_Monitoring_General_Funds` int,
  `Data_Processing_Services_All_Funds` int,
  `Data_Processing_Services_General_Funds` int,
  `Community_Services_All_Funds` int,
  `Community_Services_General_Funds` int,
  `Total_Expenditure_By_Function_All_Funds` int,
  `Total_Expenditure_By_Function_General_Funds` int,
  PRIMARY KEY (`District_Id`, `Year`)
);

CREATE TABLE `Test_Scores` (
  `District_Id` int,
  `Year` int,
  `Above_Crit_Rate_Sat` decimal(10,5),
  `Above_Crit_Rate_Act` decimal(10,5),
  `Above_Crit_Rate_Sat_Act` decimal(10,5),
  `Num_Above_Crit_Rate_Sat` int,
  `Num_Above_Crit_Rate_Act` int,
  `Num_Above_Crit_Rate_Sat_Act` int,
  `Num_Graduates_Sat` int,
  `Num_Graduates_Act` int,
  `Num_Graduates_Sat_Act` int,
  `Total_Graduates_Sat` int,
  `Total_Graduates_Act` int,
  `Total_Graduates_Sat_Act` int,
  `Participation_Rate_Sat` decimal(10,5),
  `Participation_Rate_Act` decimal(10,5),
  `Participation_Rate_Sat_Act` decimal(10,5),
  `Math_Sat` decimal(10,5),
  `Reading_Sat` decimal(10,5),
  `Writing_Sat` decimal(10,5),
  `Avg_Sat` decimal(10,5),
  `English_Act` decimal(10,5),
  `Math_Act` decimal(10,5),
  `Reading_Act` decimal(10,5),
  `Science_Act` decimal(10,5),
  `Avg_Act` decimal(10,5),
  PRIMARY KEY (`District_Id`, `Year`)
);

CREATE TABLE `Dropout_Rates` (
  `District_Id` int,
  `Year` int,
  `All_Rate` decimal(10,5),
  `African_American_Rate` decimal(10,5),
  `Asian_Rate` decimal(10,5),
  `Hispanic_Rate` decimal(10,5),
  `Multiracial_Rate` decimal(10,5),
  `American_Indian_Rate` decimal(10,5),
  `Pacific_Islander_Rate` decimal(10,5),
  `White_Rate` decimal(10,5),
  `Disadvantaged_Rate` decimal(10,5),
  `Non_Disadvantaged_Rate` decimal(10,5),
  `Female_Rate` decimal(10,5),
  `Male_Rate` decimal(10,5),
  `At_Risk_Rate` decimal(10,5),
  `Bilingual_ESL_Rate` decimal(10,5),
  `Tech_Education_Rate` decimal(10,5),
  `Foster_Care_Rate` decimal(10,5),
  `Gifted_Talented_Rate` decimal(10,5),
  `Homeless_Rate` decimal(10,5),
  `Immigrant_Rate` decimal(10,5),
  `ELL_Rate` decimal(10,5),
  `Migrant_Rate` decimal(10,5),
  `Military_Rate` decimal(10,5),
  `Overage_Rate` decimal(10,5),
  `Special_Education_Rate` decimal(10,5),
  `Title_I_Rate` decimal(10,5),
  PRIMARY KEY (`District_Id`, `Year`)
);

ALTER TABLE `Enrollment` ADD FOREIGN KEY (`District_Id`) REFERENCES `Districts` (`District_Id`);

ALTER TABLE `Classes` ADD FOREIGN KEY (`District_Id`) REFERENCES `Districts` (`District_Id`);

ALTER TABLE `Teachers` ADD FOREIGN KEY (`District_Id`) REFERENCES `Districts` (`District_Id`);

ALTER TABLE `Revenue` ADD FOREIGN KEY (`District_Id`) REFERENCES `Districts` (`District_Id`);

ALTER TABLE `Programs` ADD FOREIGN KEY (`District_Id`) REFERENCES `Districts` (`District_Id`);

ALTER TABLE `Functions` ADD FOREIGN KEY (`District_Id`) REFERENCES `Districts` (`District_Id`);

ALTER TABLE `Test_Scores` ADD FOREIGN KEY (`District_Id`) REFERENCES `Districts` (`District_Id`);

ALTER TABLE `Dropout_Rates` ADD FOREIGN KEY (`District_Id`) REFERENCES `Districts` (`District_Id`);

