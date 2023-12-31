# Generated by Django 4.2.1 on 2023-07-04 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('instrucciones', models.TextField()),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaCierre', models.DateTimeField()),
                ('activa', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('cantidadPersonas', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personas', to='backend.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('tipo', models.CharField(choices=[('Verdadero/Falso', 'Verdadero/Falso'), ('Alternativas', 'Alternativas'), ('Semi-Abierta', 'Semi-Abierta'), ('Numerica', 'Numerica'), ('Matriz', 'Matriz')], max_length=40)),
                ('dificultad', models.CharField(choices=[('baja', 'baja'), ('media', 'media'), ('alta', 'alta')], max_length=40)),
                ('tags', models.CharField(max_length=30)),
                ('orden', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('cantidadPreguntas', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('tipo', models.CharField(choices=[('Admin', 'Admin'), ('Evaluador', 'Evaluador'), ('Visualizador', 'Visualizador')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField()),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultados', to='backend.evaluacion')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultados', to='backend.grupo')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultados', to='backend.persona')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultados', to='backend.pregunta')),
            ],
        ),
        migrations.AddField(
            model_name='pregunta',
            name='prueba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='backend.prueba'),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.grupo'),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='prueba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.prueba'),
        ),
        migrations.CreateModel(
            name='Enunciado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enunciados', to='backend.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField()),
                ('contenido', models.TextField()),
                ('enunciado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternativas', to='backend.enunciado')),
            ],
        ),
    ]
