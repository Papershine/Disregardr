import data
import globalvars


def scan(json):
    for post in json:
        if data.is_scanned(post['question_id']):
            print("[PostScanner] post scanned previously, continuing")
        else:
            print("[PostScanner] scanning post")
            score, reasons = get_score(post)
            if score >= 30:
                print("[PostScanner] post exceeded threshold!")
                r = ", ".join(reasons)
                response = "[Link](%s), **Score**: %d, **Reasons**: %s" % (post['link'], score, r)
                globalvars.CHAT.send_message(response)
            else:
                print("[PostScanner] post passed filters")
            data.add_scanned(post['question_id'])


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
    if json['score'] <= -3:
        score += 20
        reasons.append('Highly downvoted')
    elif json['down_vote_count'] >= 0:
        score += 10
        reasons.append('Downvoted')

    # TODO: implement ML

    return score, reasons
