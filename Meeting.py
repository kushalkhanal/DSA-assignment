class Meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

class MeetingComparator:
    def __call__(self, o1, o2):
        if o1.end < o2.end:
            return -1
        elif o1.end > o2.end:
            return 1
        elif o1.pos < o2.pos:
            return -1
        return 1

def max_meetings(start, end, n):
    meetings = []

    for i in range(n):
        meetings.append(Meeting(start[i], end[i], i + 1))

    meetings.sort(key=lambda x: (x.end, x.pos))

    answer = [meetings[0].pos]
    limit = meetings[0].end

    for i in range(1, n):
        if meetings[i].start > limit:
            limit = meetings[i].end
            answer.append(meetings[i].pos)

    print("The order in which the meetings will be performed is:")
    print(" ".join(map(str, answer)))

if __name__ == "__main__":
    n = 6
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 5, 7, 9, 9]
    max_meetings(start, end, n)
