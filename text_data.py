def read_and_split_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    # Split the content by periods followed by any whitespace
    segments = [segment.strip() for segment in content.split('.') if segment.strip()]
    
    # Further split segments that may have contained newlines
    final_segments = []
    for segment in segments:
        sub_segments = segment.split('\n')
        final_segments.extend([sub_segment.strip() for sub_segment in sub_segments if sub_segment.strip()])
    
    return final_segments

if __name__ == "__main__":
    segments = read_and_split_file(filename)
    print(segments)  
