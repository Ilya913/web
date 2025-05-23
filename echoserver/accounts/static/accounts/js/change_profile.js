document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('profileForm');
    const emailInput = form.querySelector('[name="email"]');
    const password1Input = form.querySelector('[name="new_password1"]');

    function createErrorElement(input) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'invalid-feedback';
        input.parentNode.appendChild(errorDiv);
        return errorDiv;
    }

    async function checkFieldUniqueness(url, fieldName, fieldValue, inputElement){
        try{
            const response = await fetch(`${url}?${fieldName}=${encodeURIComponent(fieldValue)}`);

            const data = await response.json();
            return data.exists;
        } catch (error){
            console.error('Ошибка проверки: ', error);
            return false
        }
    }

    emailInput.addEventListener('input', async function() {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        let errorDiv = this.parentNode.querySelector('.invalid-feedback');
        if (!errorDiv) {
            errorDiv = createErrorElement(this);
        }

        if (!emailRegex.test(this.value)) {
            this.classList.add('is-invalid');
            errorDiv.textContent = 'Введите корректный email';
            return;
        } else {
            this.classList.remove('is-invalid');
            errorDiv.textContent = '';
        }

        const isEmailTaken = await checkFieldUniqueness(
            '/accounts/check_email/',
            'email',
            this.value,
            this
        );

        if (isEmailTaken){
            this.classList.add('is-invalid');
            errorDiv.textContent = 'Этот адресс электронной почты уже занят';
        } else{
            this.classList.remove('is-invalid');
            errorDiv.textContent = '';
        }
    });

    password1Input.addEventListener('input', function() {
        let errorDiv = this.nextElementSibling;
        if (!errorDiv || !errorDiv.classList.contains('invalid-feedback')) {
            errorDiv = createErrorElement(this);
        }

        if (this.value.length < 6){
            this.classList.add('is-invalid');
            errorDiv.textContent = 'Минимальная длина пароля 6 символов';
        } else{
            this.classList.remove('is-invalid')
            errorDiv.textContent = '';
        }
    });

    form.addEventListener('submit', function(e) {
        if (form.querySelectorAll('.is-invalid').length > 0) {
            e.preventDefault();
            alert('Исправьте ошибки в форме');
        }
    });

});