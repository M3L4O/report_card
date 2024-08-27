from report_card import ReportCard


def main():
    repo_card = ReportCard()
    grades = list(map(float, [input(f"Informe a nota {i + 1}\n~ ") for i in range(4)]))

    repo_card.add_grades(grades=grades)
    print("aprovado" if repo_card.is_approved else "reprovado")


if __name__ == "__main__":
    main()
