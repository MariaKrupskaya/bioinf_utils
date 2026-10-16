def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: str = None) -> None:
    """
    Read FASTA file with multi-line sequences
    Save it to new file, each sequence on a single line.

    Arguments:
    input_fastq: str
    output_fastq: str

    Return None. The result in the output file.
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


def parse_blast_output(input_file: str, output_file: str) -> None:
    """
    Parse the BLAST TXT output.
    For each QUERY, find the first match from the Description column.
    Sort the results alphabetically.

    Arguments:
    input_file: str
    output_file: str

    Return: None.
    """

    with open(input_file, "r") as f:
        lines = f.readlines()

    i = 0
    num_lines = len(lines)
    descriptions = set()

    while i < num_lines:
        if "Query=" in lines[i]:
            i += 1
            while i < num_lines and not lines[i].strip():
                i += 1

            while i < num_lines and "Description" not in lines[i]:
                if "Query" in lines[i]:
                    break
                i += 1

            if i < num_lines and "Description" in lines[i]:
                i += 1

            while i < num_lines and not lines[i].strip():
                i += 1

            if i < num_lines:
                hit_line = lines[i]
                print(hit_line)
                description_part = hit_line[:60].strip()
                #print(description_part)
                if description_part:
                    descriptions.add(description_part)
        i += 1

    sorted_descriptions = sorted(list(descriptions))
    #print(sorted_descriptions)
    with open(output_file, "w", encoding="utf-8") as out:
        for desc in sorted_descriptions:
            #print(desc)
            out.write(f"{desc}\n")
