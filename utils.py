import json

def load_candidates(path):
    with open(path, 'r', encoding='utf-8') as candidates:
        return json.load(candidates)


def format_candidates(candidates_list):
    result = '<pre>'
    for candidate in candidates_list:
        result += (
            f'Имя кандидата - {candidate["name"]}\n'
            f'Позиция кандидата - {candidate["position"]}\n'
            f'Навыки через запятую - {candidate["skills"]}\n\n'
        )
    result += '<pre>'

    return result

def get_by_id_candidates(candidates_list, candidate_id):
    candidate_id = int(candidate_id)
    for candidate in candidates_list:
        if candidate['pk'] == candidate_id:
            return candidate


def get_by_skill(candidates_list, skill_name):
    result = []

    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(', ')

        if skill_name.lower() in candidate_skills:
            result.append(candidate)

    return result
