def scan(json):
    for post in json['items']:
        # TODO: do not check if scanned
        score, reasons = get_score(post)
        if score >= 30:




def get_score(json):
    score = 0
    reasons = []

    # text content filters
    text = json['body_markdown']
    # TODO: find text patterns

    # very low views
    if json['view_count'] <= 15:
        score += 10
        reasons.append('Low view count')

    # negative score
    if json['score'] <= 3:
        score += 20
        reasons.append('Highly downvoted')
    elif json['down_vote_count'] >= 0:
        score += 10
        reasons.append('downvoted')

    # close vote count
    if json['close_vote_count'] >= 2:
        score += 20
        reasons.append('Multiple close votes')
    elif json['close_vote_count'] == 1:
        score += 10
        reasons.append('One close vote')

    # TODO: implement ML

    return score, reasons
