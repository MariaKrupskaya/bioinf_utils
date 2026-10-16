def filter_fastq(
        input_fastq,
        output_fastq,
        gc_bounds=(0, 100),
        length_bounds=(0, 2**32),
        quality_threshold=0
)  -> None:
  """
  Filter reads from a FASTQ file based on specified criteria.

  Arguments:
  input_fastq: str
  output_fastq: str
  gc_bounds: tuple (default (0, 100))
  length_bounds: tuple (default (0, 2**32))
  quality_threshold: int (default 0)

  Returns None. The result in the output file.
  """

  # Handle the case where a single number is passed to `gc_bounds`
  if type(gc_bounds) == int or type(gc_bounds) == float:
        gc_bounds = (0, gc_bounds)

  # Set the path for the output file
  from pathlib import Path  # without import?
  output_dir = Path("filtered")
  output_dir.mkdir(exist_ok=True)  # parents=False
  output_path = output_dir / output_fastq

  from helpers import fastq

  # Write output file
  with open(output_path, 'w') as outfile:
    for header, seq, sep, qual in fastq.read_fastq(input_fastq):
      if not fastq.check_gc_content(seq, gc_bounds):
        continue  # Fail GC-content parameer
      if not fastq.check_length(seq, length_bounds):
        continue # Fail length parameter
      if not fastq.check_quality(qual, quality_threshold):
        continue # Fail quality parameter
      outfile.write(f"{header}\n{seq}\n{sep}\n{qual}\n")
