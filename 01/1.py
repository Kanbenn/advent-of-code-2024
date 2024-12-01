def aoc1(lines):
    lefts,rights = zip(*( (int(a),int(z)) for a,z in  (l.split() for l in lines)))    
    return sum( abs(right-left) for left,right in zip(sorted(lefts),sorted(rights)) )

if __name__ == __main__:
    with open("input_sample.txt") as f:
        print("expected:", 11, "got:", aoc1(f.readlines()))