import time


class Locators:
    # Login page objects
    username_textbox_name = "UserName"
    password_textbox_name = "Password"
    login_button_xpath = "//*[@type='submit']" # xpath updated

    # SelectSite page objects
    site1_xpath = "/html/body/div/section/div/div/div/div[2]/ul/li[1]/a/div/h2"
    site2_xpath = "/html/body/div/section/div/div/div/div[2]/ul/li[2]/a/div/h2"

    # home page objects
    logout_arrow_xpath = "/*[@id='shrinkNav']/div[1]/div[2]/div[3]/a/b"
    logoutlink_text = "Log Out"

    # Xpath updated
    rmdy_studio_logo_xpath = "//div[@class ='navbar-header pointer']"
    cms_button_xpath = "//*[contains( @ href,'CMS')][contains(text(), 'Content Manager')]"
    add_folder_button_id = "AddFolderBtn"

    add_folder_button_xpath = "// *[ @ id = 'form0'] / div[2] / div[2] / input"
    folder_name_text_field_id = "FolderName"

    add_button_xpath = "//*[@id='form0']/div[2]/div[2]/input"

    add_document_button_xpath = "//*[@id='JSAddDocumentBtn']"
    add_article_xpath = "// *[ @ id = 'JSMenuAddDocumentBTN'] / li[1]"
    article_title_xpath = "//*[@id='Name']"
    article_author_id = "Author"
    article_body_xpath = "/html/body"
    article_save_button = "submitBtn"

    Go_back_to_CMS_xpath = "/html/body/div[1]/div[3]/section/div/div[1]/h1/span"

    add_video_xpath = "//*[@id='JSMenuAddDocumentBTN']/li[2]"
    add_video_title_id = "Name"
    add_video_choose_file_xpath = "//*[@id='WLpopupAddVideo']/div/div[2]/form/div[4]/div/label/strong"
    add_video_file_name_id = "filenameSpan"
    add_video_file_save_button_id = "updateButton"

    add_pdf_file_xpath = "// *[ @ id = 'JSMenuAddDocumentBTN'] / li[4]"
    add_pdf_file_title_id = "Name"
    add_pdf_choose_file_xpath = "//*[@id='AttachmentUploadForm']/div[4]/div/label/strong"
    add_pdf_file_save_xpath = "//*[@id='AttachmentUploadForm']/div[7]/div[2]/button"

    add_photo_button_xpath = "//*[@id='JSMenuAddDocumentBTN']/li[5]"
    add_photo_name_xpath = "//*[@id='Name']"
    add_photo_choose_file_button_xpath = "//*[@id='AttachmentUploadForm']/div[4]/div/label/strong"
    add_photo_save_button_xpath = "//*[@id='AttachmentUploadForm']/div[7]/div[2]/button"

    add_survey_button_xpath = "//*[@id='JSMenuAddDocumentBTN']/li[6]"
    add_survey_title_xpath = "// *[ @ id = 'Name']"
    add_survey_author_xpath = "// *[ @ id = 'Author']"
    add_survey_link_url_xpath = "//*[@id='EmbedUrl']"
    add_survey_save_button_xpath = "//*[@id='FormSurvey']/div[6]/div[2]/input"

    add_a_question_button_xpath = "//*[@id='JSMenuAddDocumentBTN']/li[7]"
    add_a_question_title_xpath = "// *[ @ id = 'Name']"
    add_a_question_xpath = "// *[ @ id = 'Question']"
    add_a_question_select_no_answers_xpath = "//*[@id='AnswersCount']"
    add_a_question_no_answers_3_xpath = "//*[@id='AnswersCount']/option[2]"
    add_a_question_answer1 = "//*[@id='AnswerOptions_0__OptionText']"
    add_a_question_answer2 = "//*[@id='AnswerOptions_1__OptionText']"
    add_a_question_answer3 = "//*[@id='AnswerOptions_2__OptionText']"
    add_a_question_save_button_xpath = "//*[@id='SendBtn']"

    # Site management Locator
    new_patient_select_test_site_id = "siteSelectionForm"
    new_patient_button_id = "newGroupBtn"
    new_patient_first_name_field_id = "FName"
    new_patient_last_name_field_id = "LName"
    new_patient_preferred_name_field_id = "PreferredName"
    new_patient_phone_number_field_id = "PrimPhone"
    new_patient_user_name_field_id = "UserName"
    new_patient_password_field_id = "Password"
    new_patient_password_confirm_id = "PasswordConfirm"
    new_patient_email_field_id = "Email"
    new_patient_location_field_id = "Location"
    new_patient_birth_date_field_id = "BirthDate"
    new_patient_save_button_id = "updateBtn"
    new_patient_preferred_language_id = "PreferredLanguageLUT"
    new_patient_preferred_english_xpath = "//*[@id='PreferredLanguageLUT']/option[2]"

    patient_site_url = "https://coach-stg.aposhealth.com/PatientSite/Account/Login"
    coach_site_ur = "https://coach-stg.aposhealth.com/CoachConsole/Account/Login"
    studio_site_url = "https://studio-stg.aposhealth.com/CoachConsole/Account/Login"
    # Coach Manager
    coach_manager_button_xpath = "/html/body/div[1]/div[3]/section/div[2]/div[2]/div[2]/div/div[3]/div/a"
    coach_manager_new_coach_button_id = "newGroupBtn"
    coach_manager_first_name_field_id = "FName"
    coach_manager_last_name_field_id = "LName"
    coach_manager_title_field_id = "Occupation"
    coach_manager_user_name_id = "UserName"
    coach_manager_password_id = "Password"
    coach_manager_password_confirm_id = "PasswordConfirm"
    coach_manager_location_field_id = "Location"
    coach_manager_birthdate_field_id = "BirthDate"
    coach_manager_gender_list_id = "Gender"
    coach_manager_gender_male_xpath = "//*[@id='Gender']/option[1]"
    coach_manager_email_field_id = "Email"
    coach_manager_test_site_xpath = "//*[@id='EditorAddform']/div[1]/div[1]/div[8]/div/div/div/div[2]/a/span[2]"
    coach_manager_external_id_field_id = "ExternalUserID"
    coach_manager_about_me_field_id = "CoachAboutMe"
    coach_manager_save_button_id = "updateBtn"
    coach_manager_coach_user_name_id = "Filter_UserName"
    coach_manager_search_coach_button_id = "searchCoachBtn"

    # Plan template
    plan_template_button_xpath = "/html/body/div[1]/div[3]/section/div[2]/div[1]/div[2]/div/div[3]/div/a"
    plan_template_create_new_template_button_xpath = "/html/body/div[1]/div[3]/section/div/div[1]/a"
    plan_template_template_name_id = "PlanName"
    plan_template_test_site_xpath = "//*[@id='frmEditBasicInfo']/div[1]/div[1]/div[3]/div/div/ul/li[2]/a/span[2]"
    plan_template_description_id = "PlanDesc"
    plan_template_save_button_xpath = "//*[@id='frmEditBasicInfo']/div[2]/div/input[1]"
    plan_template_next_first_tab_xpath = "//*[@id='WLpopupdialog']/div/div[2]/div/div/input"

    plan_template_check_box_avg_sleep_id = "CheckedYN22"
    plan_template_check_box_maximum_daily_temp_id = "CheckedYN21"
    plan_template_maximum_daily_blood_oxygen_id = "CheckedYN19"
    plan_template_maximum_daily_active_hr_id = "CheckedYN17"
    plan_template_total_weight_change = "CheckedYN12"

    plan_template_last_mood_reported_id = "LastMoodReportedYN"
    plan_template_phase_id = "PhaseYN"

    plan_template_dashboard_updated_gotit_id = "WLpopupdialog"

    plan_template_sleep_efficiency_id = "activeGraphs"
    plan_template_user_chart_save_id = "saveGraphsBtn"
    plan_template_user_app_chart_updated_popup_ok_id = "WLpopupdialog"

    plan_template_add_phase_button_id = "Phases"
    plan_template_phase_name_id = "PhaseName"
    plan_template_phase_motto_id = "PhaseMotto"
    plan_template_required_test_completed_id = "PhaseTypeLUT"
    plan_template_save_phase_button_id = "savePhaseDetails"
    plan_template_add_task_button_id = "AddTaskBTN"
    plan_template_add_tracker_xpath = "//*[@id='AddTaskBTN']/ul/li[2]/a"
    plan_template_mood_tracker_xpath = "//*[@id='WLpopupphasetaskediting']/div/div[2]/div/ul/li[4]/a/i"
    plan_template_required_task_xpath = "//*[@id='ListTasksPhase']/li/span/input"
    plan_template_publish_to_site_button_xpath = "/html/body/div[1]/div[3]/section/div[1]/div/a[4]"
    plan_template_commit_publish_to_site_xpath = "//*[@id='WLpopupdialog']/div/div[2]/div/div/input[1]"









