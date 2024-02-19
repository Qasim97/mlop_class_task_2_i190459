import pytest
from main import StudentsInMLOps

def test_enroll_drop_students():
    class_instance = StudentsInMLOps()
    
    # Test initial state
    assert class_instance.getTotalStrength() == 0, "Initial strength should be 0"
    
    # Test enrolling students
    class_instance.enrollStudents(5)
    assert class_instance.getTotalStrength() == 5, "Strength should be 5 after enrolling 5 students"
    
    # Test dropping students
    class_instance.dropStudents(2)
    assert class_instance.getTotalStrength() == 3, "Strength should be 3 after dropping 2 students"
    
    # Test dropping more students than current strength
    class_instance.dropStudents(5)
    assert class_instance.getTotalStrength() == 0, "Strength should be 0 after dropping more students than current strength"

def test_class_name():
    class_instance = StudentsInMLOps()
    assert class_instance.getClassName() == "MLOps Essentials", "Class name should be 'MLOps Essentials'"
