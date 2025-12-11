{
    'name': 'Hostel Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage Hostel rooms, students, allocation, and fees',
    'author': 'Adnan Wazir',
    'depends': ['base', 'mail'],
    'data': [
        'security/hostel_security.xml',
        'security/ir.model.access.csv',
        'views/hostel_room_views.xml',
        'views/hostel_allocation_views.xml',
        'views/hostel_fee_views.xml',
        'views/hostel_student_views.xml',
    ],
    'installable': True,
    'application': True,
}
