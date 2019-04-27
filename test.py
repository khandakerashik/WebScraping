from webscrap import wlog
from webscrap import wscrap

wlog.set_custom_log_info('html/error.log')


Home_scrap=wscrap.HomeScraper(wscrap.url_amz,wlog)
Home_scrap.retrieve_webpage()
Home_scrap.write_webpage_as_html()
Home_scrap.read_webpage_from_html()
Home_scrap.convert_data_to_bs4()
Home_scrap.print_data()
#home_scrap.parse_soup_to_simple_html()

Home_scrap=wscrap.HomeScraper(wscrap.url_bkpk,wlog)
Home_scrap.retrieve_webpage()
Home_scrap.write_webpage_as_html()
Home_scrap.read_webpage_from_html()
Home_scrap.convert_data_to_bs4()
Home_scrap.print_data()