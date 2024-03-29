
def test_insider_try(main_page,careers_page,job_page):
    main_page.go_to_home_page()
    main_page.check_main_page_is_opened()
    main_page.click_company_button()
    main_page.check_drop_down_menu_is_opened()
    main_page.click_careers_menu_button()
    careers_page.check_careers_page_is_opened()
    careers_page.check_find_your_calling_section_is_present()
    careers_page.click_see_all_teams_button()
    careers_page.check_see_all_teams_opened()
    careers_page.check_our_locations_block_is_present()
    careers_page.check_life_at_insider_section_is_present()
    #careers_page.click_qa_job()
    job_page.go_to_job_page()
    job_page.check_job_page_open()
    job_page.click_see_all_qa_jobs_button()
    job_page.select_location()
    job_page.select_department()
    job_page.check_jobs_list_present()
    job_page.check_jobs_location()
    job_page.check_jobs_department()
    job_page.click_first_view_role_button()