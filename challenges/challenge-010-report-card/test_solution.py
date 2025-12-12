# test_solution.py

import solution

def test_first_class():
    report = solution.student_report("A", 70, 65, 80)
    assert report["class"] == "1st Class"
    assert report["total"] == 215
    assert round(report["average"], 2) == round(215/3, 2)

def test_second_class():
    report = solution.student_report("B", 55, 52, 50)
    assert report["class"] == "2nd Class"

def test_pass_class():
    report = solution.student_report("C", 40, 35, 30)
    assert report["class"] == "Pass Class"

def test_fail():
    report = solution.student_report("D", 20, 30, 25)
    assert report["class"] == "Fail"

def test_exact_boundaries():
    assert solution.student_report("X", 60, 60, 60)["class"] == "1st Class"
    assert solution.student_report("Y", 50, 50, 50)["class"] == "2nd Class"
    assert solution.student_report("Z", 35, 35, 35)["class"] == "Pass Class"
