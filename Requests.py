import requests

# set the constant parameters
city = 'New York-Northern New Jersey-Long Island'
parameters = 'aqi, pm25,pm4,pm10,no,no2,ch4,so2,o3,co,bc'
parameters_array = parameters.split(',')

def api_call(start_date, end_date):
    # make API call
    url = f'https://api.openaq.org/v1/measurements?country_id=US&city={city}&date_from={start_date}&date_to={end_date}&parameters={parameters}&aggregate=hourly'
    response = requests.get(url)

    return response.json()

# get data for both years
def get_years():
    first_start_date = '2022-06-06'
    first_end_date = '2022-07-01'
    second_start_date = '2023-06-06'
    second_end_date = '2023-07-01'  

    first_data = api_call(first_start_date, first_end_date)
    second_data = api_call(second_start_date, second_end_date)

    return first_data, second_data

# print all values for specific parameter
def print_data(parameter):
    for result in first_data['results']:
        if result['parameter'] == parameter:
            print(f"Parameter: {result['parameter']}, Value: {result['value']} {result['unit']}")

# fills variables with json data for both years
first_data, second_data = get_years()

# prints first years data in JSON format
print(first_data)

# prints all parameters and their values
for parameter in parameters_array:
    print_data(parameter)


