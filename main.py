from preprocess import run_preprocessing
from statewide_dollars import run_statewide_dollars
from statewide_per_pound import run_state_per_pound
from statewide_pound_delta import run_statewide_pound_delta
from statewide_pounds import run_statewide_pounds
from statewide_value_delta import run_statewide_value_delta
from county_dollars import run_county_dollars
from county_per_pound import run_county_per_pound
from county_pound_delta import run_county_pound_delta
from county_pounds import run_county_pounds
from county_value_delta import run_county_value_delta

def main():
    run_preprocessing()
    run_statewide_dollars()
    run_state_per_pound()
    run_statewide_pound_delta()
    run_statewide_pounds()
    run_statewide_value_delta()
    run_county_dollars()
    run_county_per_pound()
    run_county_pound_delta()
    run_county_pounds()
    run_county_value_delta()
    
if __name__ == "__main__":
    main()
