import random
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

def mutate_sequence(sequence, hamming_distance):
    sequence_length = len(sequence)
    num_mutations = int(sequence_length * hamming_distance)
    positions_to_mutate = random.sample(range(sequence_length), num_mutations)
    sequence_list = list(sequence)

    for pos in positions_to_mutate:
        current_aa = sequence_list[pos]
        new_aa = random.choice([aa for aa in amino_acids if aa != current_aa])
        sequence_list[pos] = new_aa

    return ''.join(sequence_list)

def generate_mutants(sequence, hamming_distances):
    mutants = {}

    for distance in hamming_distances:
        mutant_sequence = mutate_sequence(sequence, distance)
        mutants[distance] = mutant_sequence

    return mutants

def write_to_fasta(sequence, filename):
    record = SeqRecord(Seq(sequence), id="mutant", description="")
    with open(filename, "w") as output_handle:
        SeqIO.write(record, output_handle, "fasta")

def check_hamming(input_sequence, output_sequence):
    ham=0
    length = len(input_sequence);
    for i in range(length):
        if input_sequence[i] != output_sequence[i]:
            ham+=1;
    return ham/length;

if __name__ == "__main__":
    amino_acids = "ACDEFGHIKLMNOPQRSTUVWXYZ"

    input_file = "seq1.fasta"
    input_record = SeqIO.read(input_file, "fasta")
    input_sequence = str(input_record.seq)
    print(input_sequence)

    hamming_distances = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    mutants = generate_mutants(input_sequence, hamming_distances)

    for distance, sequence in mutants.items():
        filename = f"mutant_{int(distance*10)}.fasta"
        write_to_fasta(sequence, filename)
        print(check_hamming(input_sequence,sequence))

    print("Mutants have been written to FASTA files.")
