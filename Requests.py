import requests
import json
import time

class APIError(Exception):
    pass

# Raise the custom error

# set the constant parameters
city = 'New York-Northern New Jersey-Long Island'
parameters = 'aqi,pm25,pm4,pm10,no,no2,ch4,so2,o3,co,bc'
parameters_array = parameters.split(',')

# create api url request and get json response
def api_call(parameter, start_date, end_date):
    # create API url
    url = f'https://api.openaq.org/v1/measurements?country_id=US&city={city}&date_from={start_date}&date_to={end_date}&parameter={parameter}&aggregate=hourly'

    # get call response
    response = requests.get(url)

    # return response as json
    return response.json()

# calls api_call() repeatedly for every day in the passed year using the given parameter
def get_data_for_parameter(parameter, year):
    # create empty results dict
    result_dictionary = {"results": []}

    # append to results array for 31 days
    for day in range(31):
        print("Year: " + str(year) + ", Day: " + str(day) + ", Parameter: " + str(parameter))
        if day < 9:
            apiResult = api_call(parameter, f"{year}-06-0{day}", f"{year}-06-0{day + 1}")
            if 'results' in apiResult:
                result_dictionary['results'].append(apiResult['results'])
        elif day == 9:
            apiResult = api_call(parameter, f"{year}-06-09", f"{year}-06-10")
            if 'results' in apiResult:
                result_dictionary['results'].append(apiResult['results'])
        elif day >= 10 and day < 30:
            apiResult = api_call(parameter, f"{year}-06-{day}", f"{year}-06-{day + 1}")
            if 'results' in apiResult:
                result_dictionary['results'].append(apiResult['results'])
        else:
            apiResult = api_call(parameter, f"{year}-07-01", f"{year}-07-02")
            if 'results' in apiResult:
                result_dictionary['results'].append(apiResult['results'])

    # return results array
    return result_dictionary['results']

# get data for both years
def get_years():
    # create empty dicts
    first_data = {"results": []}
    second_data = {"results": []}

    # timer start
    start_time = time.time()

    # call get_data_for_parameter for every parameter and append data to dicts
    for parameter in parameters_array:
        first_data['results'].append(get_data_for_parameter(parameter, '2022'))
        second_data['results'].append(get_data_for_parameter(parameter, '2023'))

    # print timer
    print("Elapsed time: " + str(time.time() - start_time) + "s")

    # return dicts with each years data
    return first_data, second_data

# create yearly json files
def create_json_files():
    # fills variables with json data for both years
    first_data, second_data = get_years()

    # file names for json files
    first_file_path = '2022.json'
    second_file_path = '2023.json'

    # create json files with json data in each variable
    with open(first_file_path, 'w') as file:
        json.dump(first_data, file)
    with open(second_file_path, 'w') as file:
        json.dump(second_data, file)

# query json data based on specific values
def get_parameter_value(hour, month, day, year, parameter):
    # open json file based on year
    with open(f"{year}.json") as file:
        data = json.load(file)

    # return value associated to passed date-time and parameter
    if 'results' in data:
        for result in data['results']:
            for entry in result:
                for entry2 in entry:
                    if 'date' in entry2 and 'parameter' in entry2 and 'value' in entry2 and 'unit' in entry2:
                        if entry2['date']['utc'] == f"{year}-{month}-{day}T{hour}:00:00+00:00" and entry2['parameter'] == parameter:
                            return entry2['value'], entry2['unit']

    # return error value if not found                    
    return 0, "error"

# main function
def main():
   print(get_parameter_value('12','06','07','2022','pm25'))

# for main function execution
if __name__ == "__main__":
    main()