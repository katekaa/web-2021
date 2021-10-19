from subject_area.library import Library
from subject_area.lib_lang import LibLang
from subject_area.language import Language

from operator import itemgetter

langs = [
    Language(1, "C++", "cpp", "Visual Studio"),
    Language(2, "C", "c", "Visual Studio"),
    Language(3, "C#", "cs", "Visual Studio"),
    Language(4, "Python", "py", "Visual Code"),
]

libs = [
    Library(1, "SQLite", 1),
    Library(2, "ConsolePaint", 3),
    Library(3, "Cassert", 2),
    Library(4, "NET", 3),
    Library(5, "Pandas", 4),
    Library(6, "Matplotlib", 4),
    Library(7, "Cairo", 1)
]

libs_langs = [
    LibLang(1, 1),
    LibLang(1, 3),
    LibLang(1, 4),
    LibLang(1, 7),
    LibLang(2, 1),
    LibLang(2, 3),
    LibLang(2, 7),
    LibLang(3, 2),
    LibLang(3, 4),
    LibLang(3, 7),
    LibLang(4, 5),
    LibLang(4, 6),
    LibLang(4, 7)
]


def main():
    one_to_many = [(li.name, la.name, la.extension, la.ide)
                   for li in libs
                   for la in langs
                   if li.lang_id == la.id
                   ]

    many_to_many_temp = [(la.name, ll.lang_id, ll.lib_id)
                         for la in langs
                         for ll in libs_langs
                         if la.id == ll.lang_id]

    many_to_many = [(li.name, lang_name)
                    for lang_name, lang_id, li_id in many_to_many_temp
                    for li in libs if li.id == li_id]

    print('\nЗадание Б1')
    task_1 = sorted(one_to_many, key=itemgetter(0))
    print(task_1)

    print('\nЗадание Б2')
    task_2 = []
    for la in langs:
        la_libs = list(filter(lambda elem: elem[1] == la.name, one_to_many))
        task_2.append([la.name, len(la_libs)])
    print(sorted(task_2, key=itemgetter(1)))

    print('\nЗадание Б3')
    task_3 = {}
    for li in libs:
        if (li.name.startswith('C')):
            la_libs = list(
                filter(lambda elem: elem[0] == li.name, many_to_many))
            task_3[li.name] = [x for _, x in la_libs]
    print(task_3)


if __name__ == "__main__":
    main()
