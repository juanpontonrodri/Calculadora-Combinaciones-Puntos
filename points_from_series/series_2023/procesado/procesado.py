
import pandas as pd

# Function to convert time string to seconds for sorting
def time_to_seconds(time_str):
    if ':' in time_str:
        minutes, seconds = time_str.split(':')
        return int(minutes) * 60 + float(seconds)
    return float(time_str)

# Function to determine points based on rank and whether it's a relay event
def assign_points(rank, is_relay):
    individual_points = [7, 5, 4, 3, 2, 1]
    if is_relay:
        return individual_points[rank - 1] * 2 if rank <= len(individual_points) else 0
    return individual_points[rank - 1] if rank <= len(individual_points) else 0

# Function to process the CSV and assign points
def process_swim_results(csv_path):
    # Read the CSV file
    data = pd.read_csv(csv_path, delimiter=';', header=0)
    
    # Trim spaces from data
    data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    
    # Normalize column names (remove leading/trailing spaces and convert to uppercase first letter)
    data.columns = [col.strip().capitalize() for col in data.columns]
    
    # Convert time to seconds for sorting
    #data['Tiempo'] = data['Tiempo'].apply(time_to_seconds)
    
    # Sort data by Prueba and Tiempo
    data.sort_values(by=['Prueba', 'Tiempo'], inplace=True)
    
    # Assign points
    data['Points'] = 0
    for event, group in data.groupby('Prueba'):
        is_relay = '4x' in event
        ranks = range(1, len(group) + 1)
        data.loc[group.index, 'Points'] = [assign_points(rank, is_relay) for rank in ranks]
    
    # Save the cleaned and processed data back to the original CSV to reflect trimming of spaces
    data[['Nombre', 'Club', 'Tiempo', 'Prueba']].to_csv(csv_path, index=False, sep=';')
    
    # Save the detailed results without the total points summary
    final_data = data[['Nombre', 'Club', 'Tiempo', 'Prueba', 'Points']]
    final_data.to_csv('detailed_swim_results.csv', index=False, sep=';')
    
    # Prepare and save the summary of points by club per event
    points_by_club_per_event = data.groupby(['Prueba', 'Club'])['Points'].sum().unstack(fill_value=0).reset_index()
    points_by_club_per_event.to_csv('points_by_club_per_event.csv', index=False, sep=';')
    
    # Calculate and save the total points by club
    total_points_by_club = data.groupby('Club')['Points'].sum().reset_index()
    total_points_by_club.columns = ['Club', 'Total points']
    total_points_by_club.to_csv('total_points_by_club.csv', index=False, sep=';')
    
    return final_data, points_by_club_per_event, total_points_by_club

# Call the function with the corrected file path
process_swim_results('series.csv')
