from flask import Flask

from utils import load_candidates, format_candidates, get_by_id_candidates, get_by_skill

app = Flask(__name__)

@app.route('/get')
def main():
    candidates_list = load_candidates('candidates.json')

    return format_candidates(candidates_list)


@app.route('/candidates/<candidate_id>')
def page_candidate(candidate_id):
    candidates_list = load_candidates('candidates.json')

    candidate = get_by_id_candidates(candidates_list, candidate_id)

    result = f'<img src="{candidate["picture"]}">'

    return result + format_candidates([candidate])


@app.route('/skills/<skill>')
def skills(skill):
    candidates_list = load_candidates('candidates.json')

    return format_candidates(get_by_skill(candidates_list, skill))




app.run()
