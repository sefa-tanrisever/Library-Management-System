# 📚 Library Management System

A modern, professional library management system built with **CustomTkinter** and **PostgreSQL**, featuring role-based access control, real-time statistics, and a clean, intuitive interface.

## ✨ Features

### 📖 Books Management
- Comprehensive book inventory with full CRUD operations
- Advanced search by title with language filtering
- Real-time status tracking (available, borrowed, maintenance, reserved, lost)
- Automated status management through loan workflows
- Dashboard with statistics: total books, available, borrowed, maintenance
- Multi-table joins for complete book information (author, section, publisher)

### 👥 Members Management
- Complete member lifecycle management (add, edit, delete)
- Role-based permissions (member, librarian, admin)
- Search by name or email
- Active borrower tracking
- Member dashboard showing borrowing statistics
- Phone and email contact information

### 📋 Loans Management
- Create new loans with automatic validation
- Configurable loan periods (default 14 days)
- Mark books as returned with automatic status updates
- Filter by status (borrowed, returned, overdue)
- Search across member names and book titles
- Real-time loan statistics dashboard
- Business rules enforcement:
  - Members with overdue books cannot borrow
  - Maximum 3 active loans per member
  - Only available books can be borrowed

### ⏰ Overdue Tracking
- Dedicated overdue loans view with severity indicators
- Automatic overdue status updates
- Color-coded severity levels:
  - **Critical** (30+ days): Red, bold
  - **Moderate** (7-30 days): Orange
  - **Recent** (≤7 days): Yellow
- Member contact information for follow-ups
- One-click status refresh

### 🔐 Authentication & Authorization
- Dual authentication system (staff and members)
- Secure login with role-based access
- Staff accounts: librarian and admin roles
- Member accounts: limited read-only access
- Session management with logout functionality

### 👤 Member Portal
- Browse books catalog (read-only)
- View personal loan history
- Check active loans and due dates
- Monitor overdue status
- Language filtering for book search

## 🎨 UI/UX Design

### Modern Interface
- **Clean, professional design** with consistent color scheme
- **Primary color**: Forest Green (#1a5f3d) for trust and stability
- **Dashboard cards** with real-time statistics and emoji indicators
- **Advanced search and filtering** with instant results
- **Modal dialogs** for create/edit operations
- **Color-coded status indicators** for quick visual feedback
- **Responsive layout** that adapts to window size
- **Zebra striping** in tables for better readability
- **Hover effects** and smooth transitions

### Accessibility Features
- High contrast text and backgrounds
- Clear visual hierarchy
- Consistent button placement
- Descriptive labels and placeholders
- Error messages with actionable guidance

## 🏗️ Architecture

### Project Structure
```
Library Management System/
├── .env                          # Environment configuration (gitignored)
├── .env.example                  # Example environment template
├── .gitignore                   # Git ignore rules
├── README.md                    # This file
│
├── app/
│   ├── __init__.py
│   ├── main.py                  # Application entry point
│   ├── db.py                    # Database connection manager
│   │
│   ├── repositories/            # Data access layer
│   │   ├── __init__.py
│   │   ├── auth_repo.py         # Authentication queries
│   │   ├── books_repo.py        # Books CRUD operations
│   │   ├── members_repo.py      # Members management
│   │   ├── loans_repo.py        # Loans processing
│   │   ├── member_loans_repo.py # Member-specific loan queries
│   │   └── overdue_repo.py      # Overdue tracking
│   │
│   └── ui/                      # User interface layer
│       ├── __init__.py
│       ├── login_window.py      # Login/authentication screen
│       ├── app_window.py        # Main application window
│       ├── modern_table_styles.py # Reusable UI components
│       ├── books_view.py        # Books management (staff)
│       ├── members_view.py      # Members management (staff)
│       ├── loans_view.py        # Loans management (staff)
│       ├── overdue_view.py      # Overdue tracking (staff)
│       ├── member_books_view.py # Book browsing (member)
│       └── member_loans_view.py # Personal loans (member)
│
└── sql/                         # Database scripts
    ├── 01_create_database.sql   # Database creation
    ├── 02_schema.sql            # Tables and constraints
    ├── 03_seed.sql              # Sample data (200 books, 10 members)
    ├── 04_routines.sql          # Stored functions and procedures
    ├── 05_integrity.sql         # Additional integrity constraints
    └── 06_business_rules.sql    # Business logic triggers
```

### Design Patterns
- **Repository Pattern**: Clean separation between UI and data access
- **MVC Architecture**: Model (DB/Repositories), View (UI), Controller (Event Handlers)
- **Factory Pattern**: Reusable UI component creation (StatCard, ModernTable)
- **Context Managers**: Automatic resource cleanup for database connections

### Technology Stack
- **Frontend**: CustomTkinter (modern Tkinter wrapper)
- **Backend**: Python 3.8+
- **Database**: PostgreSQL 15.15
- **DB Driver**: psycopg 3.x
- **Environment**: python-dotenv for configuration

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL 15.15
- pip package manager

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd "Library Management System"
```

### Step 2: Install Dependencies
```bash
pip install customtkinter
pip install "psycopg[binary]"
pip install python-dotenv
```

### Step 3: Database Setup

#### Create the database:
```bash
psql -U postgres -f sql/01_create_database.sql
```

#### Create the schema:
```bash
psql -U postgres -d LibraryManagement -f sql/02_schema.sql
```

#### Seed initial data:
```bash
psql -U postgres -d LibraryManagement -f sql/03_seed.sql
```

#### Create functions and procedures:
```bash
psql -U postgres -d LibraryManagement -f sql/04_routines.sql
```

#### Add integrity constraints:
```bash
psql -U postgres -d LibraryManagement -f sql/05_integrity.sql
```

#### Add business rules:
```bash
psql -U postgres -d LibraryManagement -f sql/06_business_rules.sql
```

### Step 4: Configure Environment

Create a `.env` file in the project root:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=LibraryManagement
DB_USER=postgres
DB_PASSWORD=your_password_here
```

### Step 5: Run the Application
```bash
python -m app.main
```

Or from the app directory:
```bash
cd app
python main.py
```

## 🔑 Demo Accounts

### Staff Account (Full Access)
- **Email**: staff1@library.com
- **Password**: 1234
- **Role**: Librarian
- **Access**: Books, Members, Loans, Overdue management

### Member Account (Limited Access)
- **Email**: ali@example.com
- **Password**: 1234
- **Role**: Member
- **Access**: Browse books, view personal loans

## 📊 Database Schema

### Core Tables
- **books**: Book inventory with status tracking
- **author**: Author information
- **section**: Book categorization
- **publisher**: Publisher details
- **member**: Library member accounts
- **librarian**: Staff accounts
- **permission**: Role-based permissions
- **loan**: Loan transaction records

### Key Relationships
- Books → Author (many-to-one)
- Books → Section (many-to-one)
- Books → Publisher (many-to-one, optional)
- Loan → Member (many-to-one)
- Loan → Books (many-to-one)
- Member/Librarian → Permission (many-to-one)

### Business Rules (Enforced by Triggers)
1. A book can have at most ONE active loan at a time
2. Cannot manually set borrowed book to 'available' (must use Return workflow)
3. Members with overdue books cannot borrow new books
4. Maximum 3 active loans per member
5. Automatic overdue status updates when due date passes

### Stored Functions
- `list_overdue_loans()`: Returns all overdue loans with member/book details
- `can_member_borrow()`: Validates member borrowing eligibility

### Stored Procedures
- `mark_overdue_loans()`: Updates loan status for overdue items

## 🎯 Usage Guide

### For Staff/Librarians

#### Books Management
1. Navigate to **Books** section
2. Use search bar to find books by title or filter by language
3. Click **+ New Book** to add a book
4. Select a book and click **Edit** to modify details
5. Select a book and click **Delete** to remove (if no active loans)
6. View real-time statistics: Total, Available, Borrowed, Maintenance

#### Members Management
1. Navigate to **Members** section
2. Search members by name or email
3. Click **+ New Member** to register new members
4. Edit member details or change roles (member/librarian/admin)
5. Delete members (only if no loan history)

#### Loans Management
1. Go to **Loans** section
2. Click **+ New Loan** to create a new loan:
   - Select member from dropdown
   - Select available book from dropdown
   - Set loan period (default 14 days)
   - System validates member eligibility automatically
3. View all loans with filters (All/Borrowed/Returned/Overdue)
4. Select a loan and click **Mark as Returned** to process returns
5. System automatically:
   - Updates book status to 'available'
   - Records return date
   - Frees up member's loan slot

#### Overdue Tracking
1. Visit **Overdue** section
2. View all overdue loans with severity indicators:
   - 🚨 Critical (30+ days) - Red, bold
   - ⚠️ Moderate (7-30 days) - Orange
   - ⏰ Recent (≤7 days) - Yellow
3. Click **🔄 Update Overdue Status** to refresh from database
4. Access member contact info for follow-ups

### For Members

#### Browse Books
1. Login with member credentials
2. Navigate to **Browse Books** (default page)
3. Search books by title
4. Filter by language
5. View book details including availability status

#### View Personal Loans
1. Navigate to **My Loans**
2. View all personal loan history
3. Check active loans and due dates
4. Monitor overdue status
5. See borrowing statistics

## 🔧 Customization

### Changing Theme Colors
Edit color values in `app/ui/app_window.py` and `app/ui/modern_table_styles.py`:
```python
fg_color="#1a5f3d"      # Primary green
hover_color="#236b49"   # Hover green
```

### Adjusting Default Loan Period
Modify in `app/ui/loans_view.py`:
```python
self.days_entry.insert(0, "14")  # Change to desired days
```

### Database Connection
Update credentials in `.env` file (never commit this file to version control).

### Adding New Book Categories
Insert into section table:
```sql
INSERT INTO section (section_name) VALUES ('New Category');
```

## 🛡️ Security Notes

⚠️ **Important**: This is an educational/demonstration project. For production use:

1. **Password Security**: Implement proper password hashing (bcrypt, argon2, etc.)
   - Current: Plain text storage (NOT SECURE)
   - Recommended: Use `passlib` or `bcrypt` libraries

2. **SQL Injection**: Already protected via parameterized queries
   - All user inputs are sanitized through psycopg parameters

3. **Session Management**: Basic implementation
   - Consider adding session timeouts
   - Implement CSRF protection for web deployments

4. **Role-Based Access Control**: Partially implemented
   - UI enforces role-based views
   - Database constraints provide additional security
   - Consider adding row-level security in PostgreSQL

5. **Environment Variables**: 
   - Keep `.env` file secure and gitignored
   - Use different credentials for development/production

## 🐛 Troubleshooting

### Database Connection Issues
**Problem**: Cannot connect to PostgreSQL
**Solutions**:
- Verify PostgreSQL service is running: `pg_ctl status`
- Check credentials in `.env` file match database user
- Ensure database exists: `psql -U postgres -l`
- Check PostgreSQL is listening on correct port (default 5432)
- Verify firewall allows PostgreSQL connections

### Import Errors
**Problem**: `ModuleNotFoundError` when running application
**Solutions**:
- Verify all dependencies are installed: `pip list`
- Check Python version: `python --version` (needs 3.8+)
- Ensure running from correct directory
- Try: `pip install --upgrade customtkinter psycopg python-dotenv`
- Verify `__init__.py` files exist in all package directories

### UI Not Loading
**Problem**: Blank window or UI elements missing
**Solutions**:
- Verify CustomTkinter installation: `python -c "import customtkinter"`
- Check Python version compatibility (3.8+)
- Try running with: `python -m app.main` instead of `python main.py`
- Check terminal for error messages
- Ensure display/graphics drivers are up to date

### Business Rule Violations
**Problem**: Cannot create loan or update book status
**Expected Behavior**: This is by design when:
- Member has overdue books (cannot borrow)
- Member has 3 active loans (at maximum)
- Book is borrowed (cannot manually change to available)
- Book has active loan (must return via Loans workflow)

### Data Integrity Issues
**Problem**: Orphaned records or inconsistent states
**Solutions**:
- Run integrity constraints: `sql/05_integrity.sql`
- Check for trigger errors in PostgreSQL logs
- Verify foreign key relationships
- Use proper return workflow (don't manually update statuses)

## 📈 Future Enhancements

### Planned Features
- [ ] Email notifications for overdue books
- [ ] Fine calculation and payment tracking
- [ ] Book reservation system
- [ ] ISBN barcode scanning
- [ ] Export reports to PDF/Excel
- [ ] Advanced analytics dashboard
- [ ] Book recommendations based on history
- [ ] Multi-branch support
- [ ] RESTful API for mobile apps
- [ ] Web-based interface using Flask/Django

### Potential Improvements
- [ ] Implement password hashing
- [ ] Add pagination for large datasets
- [ ] Enhanced search (fuzzy matching, full-text)
- [ ] Book cover image support
- [ ] Member photo/ID upload
- [ ] Audit logging for all operations
- [ ] Backup and restore functionality
- [ ] Dark/light theme toggle
- [ ] Multi-language support (i18n)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Bug fixes
- Feature enhancements
- Documentation improvements
- UI/UX improvements
- Performance optimizations

### Development Guidelines
1. Follow PEP 8 style guide
2. Add docstrings to all functions
3. Write unit tests for new features
4. Update README for significant changes
5. Keep commits atomic and well-described

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created as a demonstration of modern desktop application development with Python, PostgreSQL, and CustomTkinter.

## 🙏 Acknowledgments

- **CustomTkinter**: Modern UI framework
- **psycopg**: Reliable PostgreSQL adapter
- **PostgreSQL**: Robust database system
- **Python**: Versatile programming language

---

**Built with ️✌️using Python, CustomTkinter, and PostgreSQL**

*For questions, issues, or suggestions, please open an issue on the project repository.*
