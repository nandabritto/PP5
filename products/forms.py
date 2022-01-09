from django import forms

PRODUCT_CHOICES= [
    ('product1', 'PLACEHOLDER1'),
    ('Product2', 'PLACEHOLDER2'),
    ('product3', 'PLACEHOLDER3'),
    ('product4', 'PLACEHOLDER4'),
    ('product5', 'PLACEHOLDER5'),
    ('Product6', 'PLACEHOLDER6'),
    ('product7', 'PLACEHOLDER7'),
    ('product8', 'PLACEHOLDER8'),
    ('produc9', 'PLACEHOLDER9'),
    ('Product10', 'PLACEHOLDER10'),    
    ]

class UserForm(forms.Form):
    favorite_fruit= forms.MultipleChoiceField(label='Choose the products for your box', widget=forms.CheckboxSelectMultiple,choices=PRODUCT_CHOICES)