import unidecode


class Candidate:
    def __init__(self, name: str, score: str, candidate_url: str):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        self.name = name

        if not isinstance(score, str):
            raise ValueError("Score must come as string first")
        self.score = score

        if not isinstance(candidate_url, str):
            raise ValueError("Candidate_url must be a string")
        self.candidate_url = candidate_url

    def _process_name(self, name):
        name = name.strip()
        name = name.lower()
        # Remove accents
        name = unidecode.unidecode(name)
        return name

    def _process_score(self, score):
        return float(score)

    def _take_cpf_from_url(self):
        return self.candidate_url[-14:]

    def get_cleaned_candidate(self):
        return {
            'name': self._process_name(self.name),
            'score': self._process_score(self.score),
            'cpf': self._take_cpf_from_url(),
        }
