import os

def concatenate_files(source_directory, output_file, file_order):
    """Concatenate files in a specific order from a given directory."""
    with open(output_file, 'a') as outfile:  # Append mode to add each airfield's content sequentially
        for filename in file_order:
            file_path = os.path.join(source_directory, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as infile:
                    for line in infile:
                        stripped_line = line.strip()
                        if stripped_line:
                            if stripped_line.startswith('//&preserve'):
                                # Remove the //&preserve prefix but keep the // and the rest of the line
                                stripped_line = '//' + stripped_line[len('//&preserve'):].strip()
                            elif stripped_line.startswith('//'):
                                # Skip lines starting with // that don't start with //&preserve
                                continue
                            outfile.write(stripped_line + '\n')  # Write the cleaned line

def main():
    base_dir = '.data/GroundRadarPluginMaps'
    targets = [
        ('Maps', 'OMAE/Plugins/Ground Radar Plugin/GRpluginMaps.txt', ['regions.txt', 'geo.txt', 'freetext.txt', 'nets.txt']),
        ('Stands', 'OMAE/Plugins/Ground Radar Plugin/GRpluginStands.txt', ['stands.txt']),
    ]

    for source_subdir, target_file, file_order in targets:
        source_directory = os.path.join(base_dir, source_subdir)
        # Discover airfields in the directory
        airfields = sorted(
            [d for d in os.listdir(source_directory) if os.path.isdir(os.path.join(source_directory, d))]
        )
        
        print(f'Building {target_file} from {source_directory}')
        # Ensure the output file starts empty
        with open(target_file, 'w') as final_output:
            pass

        # Process each airfield directory
        for airfield in airfields:
            airfield_dir = os.path.join(source_directory, airfield)
            print(f'Processing airfield: {airfield}')
            concatenate_files(airfield_dir, target_file, file_order)

        print(f'{target_file} built successfully.')

if __name__ == '__main__':
    main()
