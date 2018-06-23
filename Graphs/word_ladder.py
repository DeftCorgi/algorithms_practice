from Graph import Graph, Vertex


def create_word_ladder_graph(filename):
    "creates buckets, and places word into appropriate bucket then connect words from same bucket"
    buckets = {}
    f = open(filename, 'r')

    # create buckets of words off by one letter
    for line in f.readlines():
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in buckets:
                buckets[bucket].append(word)
            else:
                buckets[bucket] = [word]
    f.close()

    # create graph with edges connecting words in buckets
    g = Graph()
    for bucket in buckets:
        for word1 in buckets[bucket]:
            for word2 in buckets[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


def test_bfs(filename, g):
    f = open(filename, 'r')
    for line in f.readlines():
        start, goal = line.strip().split()
        result = g.bfs(start, goal)
        result = [v.key for v in result]
        print("Input: {} {}, Output: {}".format(start, goal, result))


if __name__ == '__main__':
    g = create_word_ladder_graph('word_ladder_dict.txt')
    test_bfs('word_ladder_test.txt', g)
