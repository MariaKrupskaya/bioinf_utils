def read_fastq(file_path):
    """Read FASTQ file one by one."""
    with open(file_path, 'r') as f:
        while True:
            header = f.readline()
            if not header:
                break
            if not header.startswith('@'):
                break

            header = header.strip()
            seq = f.readline().strip()
            sep = f.readline().strip()
            if not sep.startswith('+'):
                break
            qual = f.readline().strip()

            yield header, seq, sep, qual


def check_gc_content(sequence, gc_bounds):
    """Verify the GC content is within the limits."""
    if len(sequence) == 0:
        return False
    gc_percent = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
    return gc_bounds[0] <= gc_percent <= gc_bounds[1]


def check_length(sequence, length_bounds):
    return length_bounds[0] <= len(sequence) <= length_bounds[1]


def check_quality(quality_scores, threshold):
    quality_scores = [ord(c) - 33 for c in quality_scores]
    avg_quality = sum(quality_scores) / len(quality_scores)
    return avg_quality >= threshold
