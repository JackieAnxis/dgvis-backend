import json


def test():
    f = open('../graph.json')
    graph = json.load(f)
    f.close()
    links = graph['links']
    links_set = set()
    print(len(graph['nodes']), len(graph['links']))
    # for link in links:
    #     t0 = str(link['source']) + '-' + str(link['target'])
    #     t1 = str(link['target']) + '-' + str(link['source'])
    #     if t0 in links_set:
    #         print(t0)
    #     else:
    #         links_set.add(t0)
    #         links_set.add(t1)
    #     if t0 == t1:
    #         print(t0)


if __name__ == '__main__':
    test()
