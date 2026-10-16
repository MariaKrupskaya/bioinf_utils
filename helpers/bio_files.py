def convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None) -> None:
    """
    Read FASTA file with multi-line sequences
    Save it to new file, each sequence on a single line.

    Arguments:
    input_fastq: str
    output_fastq: str

    Returns None. The result in the output file.
    """

    from pathlib import Path
    if output_fasta is None:
        input_path = Path(input_fasta)
        name = input_path.stem
        output_fasta = f"{name}_oneline.fasta"

    with (
        open(input_fasta, 'r') as input_f,
        open(output_fasta, 'w') as output_f
    ):
        current_seq = []
        for line in input_f:
            line = line.strip()
            if not line:
                continue

            if line.startswith('>'):
                if current_seq:
                    output_f.write(''.join(current_seq) + '\n')
                    current_seq = []
                output_f.write(line + '\n')
            else:
                current_seq.append(line)

        if current_seq:
            output_f.write(''.join(current_seq) + '\n')
            