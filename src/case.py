import requests

host_url = 'http://localhost:9999'          # Make sure the RIT client uses the same 9999 port
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed
class ApiException(Exception):
    pass

# function requires a requests.Session() object as the ses argument with a loaded API_KEY
def get_case_response ( ses, url_end, param, full=0 ):
    response = ses.get( base_url + url_end )
    if response.ok:
        case = response.json()
        if full == 1:
            return case
        return case[param]
    raise ApiException('Authorization Error: Please check API key.')

def get_name( ses ):
    get_case_response( ses, '/case', 'name')

def get_status( ses ):
    get_case_response( ses, '/case', 'status')

def get_tick( ses ):
    get_case_response( ses, '/case', 'tick')

def get_period( ses ):
    get_case_response( ses, '/case', 'period')

def get_total_periods( ses ):
    get_case_response( ses, '/case', 'get_periods')

def get_ticks_per_period( ses ):
    get_case_response( ses, '/case', 'ticks_per_period')

# returns json object containing full info on case
def get_case_all( ses ):
    get_case_response( ses, '/case', '', 1 )

# functions for information on case limits
# checking if a trade_limit is actually enforced
def trade_lim_enforce_chk ():
    if get_case_response( ses, '/case', 'is_enforce_trading_limits') == True:
        return True
    return False

def get_gross( ses ):
    if trade_lim_enforce_chk() == True:
        get_case_response( ses, '/limits', 'gross')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg

def get_set( ses ):
    if trade_lim_enforce_chk() == True:
        get_case_response( ses, '/limits', 'set')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg

def get_gross_lim( ses ):
    if trade_lim_enforce_chk() == True:
        get_case_response( ses, '/limits', 'gross_limit')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg

def get_set_limit( ses ):
    if trade_lim_enforce_chk() == True:
        get_case_response( ses, '/limits', 'set_limit')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg

def get_gross_fine( ses ):
    if trade_lim_enforce_chk() == True:
        get_case_response( ses, '/limits', 'gross_fine')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg

def get_set_fine( ses ):
    if trade_lim_enforce_chk() == True:
        get_case_response( ses, '/limits', 'set_fine')
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg

def get_limits_case_all( ses ):
    if trade_lim_enforce_chk() == True:
        get_case_response( ses, '/limits', '', 1)
    else:
        no_lim_msg = "No trading limits for the current case"
        return no_lim_msg
