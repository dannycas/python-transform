# Przewodnik Uczestnictwa (Contributing)

Dziękujemy zainteresowania w przyczynieniu się do projektu python-transform!

## Jak możesz pomóc?

### Zgłaszanie błędów

Jeśli znalazłeś błąd, otwórz issue z:
- Opisem problemu
- Krokami reprodukcji
- Oczekiwanym zachowaniem
- Rzeczywistym zachowaniem
- Informacjami o systemie (OS, wersja Pythona, itd.)

### Sugestie ulepszeń

Jeśli masz pomysł na nową funkcjonalność:
- Otwórz issue z tytułem: `[FEATURE REQUEST]`
- Opisz problem, który by to rozwiązało
- Zaproponuj rozwiązanie (opcjonalnie)

### Przygotowywanie Pull Requests

1. **Fork repozytorium**
   ```bash
   git clone https://github.com/yourusername/python-transform.git
   ```

2. **Stwórz branch dla funkcji/poprawki**
   ```bash
   git checkout -b feature/moja-nowa-funkcja
   ```

3. **Zainstaluj zależności developerskie**
   ```bash
   pip install -r requirements.txt
   pip install pytest flake8
   ```

4. **Wprowadź zmiany**
   - Pisz czytelny kod
   - Dodaj docstringi
   - Utrzymuj style istniejącego kodu

5. **Uruchom testy**
   ```bash
   python -m pytest tests/
   ```

6. **Sprawdź jakość kodu**
   ```bash
   flake8 --max-line-length=120 .
   ```

7. **Commitnij zmiany**
   ```bash
   git commit -am 'Dodaj moją nową funkcję'
   ```

8. **Push do brancha**
   ```bash
   git push origin feature/moja-nowa-funkcja
   ```

9. **Otwórz Pull Request**
   - Opisz co zmieniłeś
   - Linkuj powiązane issues

## Standardy kodowania

- PEP 8 compliance (max 120 znaków na linię)
- Docstringi dla wszystkich funkcji/klas
- Type hints gdzie to możliwe
- Testy dla nowych funkcjonalności

## Proces reviewu

Wszystkie PR będą przejście review przed zaakceptowaniem:
- Sprawdzenie kodu
- Testy
- Dokumentacja
- Zgodność ze standardami

## Pytania?

Otwórz issue lub skontaktuj się z maintainerami.

Dziękujemy za wkład! 🎉
