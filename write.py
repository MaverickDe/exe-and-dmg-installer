import pandas as pd
import os
def writetofile(new_data,csv_file):


   

  

    # Convert the new data to a DataFrame
    new_df = pd.DataFrame(new_data)

    # Specify the CSV file name
  

    # Check if the file exists
    if os.path.exists(csv_file):
        # If the file exists, read the existing CSV file into a DataFrame
        existing_df = pd.read_csv(csv_file)
        # Append the new data to the existing DataFrame
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    else:
        # If the file does not exist, create a new DataFrame
        updated_df = new_df

    # Write the updated DataFrame back to the CSV file
    updated_df.to_csv(csv_file, index=False)

    print(f"Data has been written to {csv_file}")
    print("k")
    # driver.quit()