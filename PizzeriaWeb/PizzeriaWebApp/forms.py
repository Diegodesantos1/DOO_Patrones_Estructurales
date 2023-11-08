from django import forms


class PizzaBuilderForm(forms.Form):
    MASA_CHOICES = [
        ('Delgada', 'Delgada'),
        ('Pan', 'Pan'),
        ('Fermentada', 'Fermentada'),
        ('Sin gluten', 'Sin gluten'),
    ]
    SALSA_CHOICES = [
        ('Tomate', 'Tomate'),
        ('Pesto', 'Pesto'),
        ('BBQ', 'BBQ'),
        ('Yogur', 'Yogur'),
        ('Carbonara', 'Carbonara'),
        ('Sin salsa', 'Sin salsa'),
    ]
    INGREDIENTES_CHOICES = [
        ('Jamón', 'Jamón'),
        ('Queso', 'Queso'),
        ('Champiñones', 'Champiñones'),
        ('Tomate', 'Tomate'),
        ('Pimiento', 'Pimiento'),
        ('Cebolla', 'Cebolla'),
        ('Piña', 'Piña'),
        ('Pepperoni', 'Pepperoni'),
        ('Salami', 'Salami'),
        ('Aceitunas', 'Aceitunas'),
        ('Pollo', 'Pollo'),
        ('Carne picada', 'Carne picada'),
        ('Chorizo', 'Chorizo'),
        ('Tocino', 'Tocino'),
        ('Jalapeños', 'Jalapeños'),
    ]
    TECNICA_CHOICES = [
        ('Horno tradicional', 'Horno tradicional'),
        ('Cocina a la leña', 'Cocina a la leña'),
        ('Cocina molecular', 'Cocina molecular'),
    ]
    PRESENTACION_CHOICES = [
        ('Clásica', 'Clásica'),
        ('Artística', 'Artística'),
        ('Personalizada', 'Personalizada'),
    ]
    MARIDAJE_CHOICES = [
        ('Vino', 'Vino'),
        ('Cerveza', 'Cerveza'),
        ('Coctel', 'Coctel'),
        ('Refresco', 'Refresco'),
        ('Agua', 'Agua'),
    ]

    EXTRAS_CHOICES = [
        ('Queso extra', 'Queso extra'),
        ('Salsa extra', 'Salsa extra'),
        ('Borde de queso', 'Borde de queso'),
    ]

    masa = forms.ChoiceField(choices=[('', 'Seleccione una masa')] + MASA_CHOICES)
    salsa = forms.ChoiceField(choices=[('', 'Seleccione una salsa')] + SALSA_CHOICES)
    ingredientes = forms.MultipleChoiceField(
        choices=INGREDIENTES_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
    tecnica = forms.ChoiceField(choices=[('', 'Seleccione una técnica')] + TECNICA_CHOICES)
    presentacion = forms.ChoiceField(choices=[('', 'Seleccione una presentación')] + PRESENTACION_CHOICES)
    maridaje = forms.ChoiceField(
        choices=[('', 'Seleccione un maridaje')] + MARIDAJE_CHOICES,
        required=False
    )
    extras = forms.MultipleChoiceField(
        choices=EXTRAS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

