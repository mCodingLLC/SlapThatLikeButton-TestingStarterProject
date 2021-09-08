import enum


class LikeState(enum.Enum):
    empty = enum.auto()
    liked = enum.auto()
    disliked = enum.auto()


slap_like_transitions = {
    LikeState.empty: LikeState.liked,
    LikeState.liked: LikeState.empty,
    LikeState.disliked: LikeState.liked,
}

slap_dislike_transitions = {
    LikeState.empty: LikeState.disliked,
    LikeState.liked: LikeState.disliked,
    LikeState.disliked: LikeState.empty,
}


def slap_like(s: LikeState) -> LikeState:
    return slap_like_transitions[s]


def slap_dislike(s: LikeState) -> LikeState:
    return slap_dislike_transitions[s]


def slap_many(s: LikeState, slaps: str) -> LikeState:
    for c in slaps:
        c = c.lower()
        if c == 'l':
            s = slap_like(s)
        elif c == 'd':
            s = slap_dislike(s)
        else:
            raise ValueError('invalid slap')
    return s
