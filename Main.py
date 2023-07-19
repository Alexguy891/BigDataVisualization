import HeatMap
import Mattvis
import SingleDay
import Requests

def main():
    # initialize user input
    user_input = ""

    # continuously get user input until quit chosen
    while user_input.lower() != "q":
        user_input = input("[g]ather API data | [h]eat map | [d]aily graph | [s]ingle day graph | [q]uit  (g/h/d/s/o/q): ")

        # call corresponding main function for given choice
        if user_input.lower() == "g":
            Requests.create_json_files()
        elif user_input.lower() == "h":
            HeatMap.run_heatmap()
        elif user_input.lower() == "d":
            Mattvis.run_mattvis()
        elif user_input.lower() == "s":
            SingleDay.run_aqi_visualization()
        elif user_input.lower() == "o":
            Mattvis.run_mattvis()
        elif user_input != "q":
            print("invalid input.")

if __name__ == "__main__":
    main()