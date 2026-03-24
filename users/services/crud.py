from django.contrib.auth import get_user_model


def create_user(
    email: str,
    password: str = None,
    first_name: str = "",
    surname: str = "",
    is_staff: bool = False,
    is_superuser: bool = False,
    is_active: bool = True,
    **extra_fields,
):
    User = get_user_model()

    user = User(
        email=email,
        first_name=first_name,
        surname=surname,
        is_superuser=is_superuser,
        is_staff=is_staff,
        is_active=is_active,
        **extra_fields,
    )

    if password:
        user.set_password(password)
    else:
        user.set_unusable_password()

    user.full_clean()
    user.save()
    return user
