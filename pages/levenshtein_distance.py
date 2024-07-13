from utils import get_data_file_path
import streamlit as st


def load_vocab(file_name):
    file_path = get_data_file_path(file_name)
    with open(file_path, "r") as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


def levenshtein_distance(token1, token2):
    def initialize_distances(token1, token2):
        distances = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]
        for t1 in range(len(token1) + 1):
            distances[t1][0] = t1
        for t2 in range(len(token2) + 1):
            distances[0][t2] = t2
        return distances

    def compute_costs(distances, token1, token2):
        for t1 in range(1, len(token1) + 1):
            for t2 in range(1, len(token2) + 1):
                if token1[t1 - 1] == token2[t2 - 1]:
                    distances[t1][t2] = distances[t1 - 1][t2 - 1]
                else:
                    a = distances[t1][t2 - 1]
                    b = distances[t1 - 1][t2]
                    c = distances[t1 - 1][t2 - 1]
                    distances[t1][t2] = min(a, b, c) + 1

    distances = initialize_distances(token1, token2)
    compute_costs(distances, token1, token2)
    return distances[len(token1)][len(token2)]


def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input("Word: ")
    vocabs = load_vocab("vocab.txt")

    if st.button("Compute "):
        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        # sorted by distance
        sorted_distences = dict(
            sorted(leven_distances.items(), key=lambda item: item[1])
        )
        correct_word = list(sorted_distences.keys())[0]
        st.write("Correct word: ", correct_word)

        col1, col2 = st.columns(2)
        col1.write("Vocabulary: ")
        col1.write(vocabs)

        col2.write("Distances: ")
        col2.write(sorted_distences)


if __name__ == "__main__":
    main()
