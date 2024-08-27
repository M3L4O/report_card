from dataclasses import dataclass, field


@dataclass
class ReportCard:
    grades: list[float] = field(default_factory=list)
    weights: list[float] = field(default_factory=lambda: [0.4, 0.3, 0.3])
    weighted_grades: list[float] = field(default_factory=list)
    final_grade_used: bool = False

    def add_grades(self, grades: list[float]):
        self.grades = grades
        self.weighted_grades = [
            weight * grade for weight, grade in zip(self.weights, self.grades)
        ]

    @property
    def is_approved(self):
        if sum(self.weighted_grades) >= 60:
            return True
        elif not self.final_grade_used:
            self.final_grade_used = True

            final_grade_weighted = [self.grades[-1] * weight for weight in self.weights]
            bigger_final_grade = max(final_grade_weighted)
            max_index = final_grade_weighted.index(bigger_final_grade)

            if self.weighted_grades[max_index] > bigger_final_grade:
                return False

            self.weighted_grades[max_index] = bigger_final_grade

            return sum(self.weighted_grades) >= 60

        return False
