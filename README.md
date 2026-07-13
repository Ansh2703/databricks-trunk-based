# 🚀 Trunk-Based Development with Databricks

This project demonstrates **Trunk-Based Development** strategy with Databricks Bundles (DABs) and GitHub Actions CI/CD.

---

## 📖 **What is Trunk-Based Development?**

Trunk-based development is a source control branching model where developers:
- Merge small, frequent updates directly to a single **main branch** (the "trunk")
- Create short-lived feature branches (1-2 days max)
- Deploy to production on **every merge to main**
- Use feature flags for incomplete features
- Maintain high test coverage and CI quality gates

---

## 🌳 **Branch Strategy**

```
main (trunk)
  ├── feature/add-customer-validation  (short-lived, 1-2 days)
  ├── feature/fix-aggregation-bug      (short-lived, hours)
  └── feature/update-schema            (short-lived, 1 day)
```

### **Key Principles:**
- ✅ **One main branch** (main) - always deployable
- ✅ **Short-lived feature branches** - merge within 1-2 days
- ✅ **Direct to production** - every merge deploys to prod
- ✅ **High test coverage** - CI must pass before merge
- ❌ **No dev/staging branches** - use feature flags instead
- ❌ **No long-lived branches** - keep branches small

---

## 🏗️ **Project Structure**

```
databricks-trunk-based/
├── .github/
│   └── workflows/
│       └── deploy.yml           # Simplified CI/CD (main branch only)
├── notebooks/
│   ├── bronze_ingestion.py      # Raw data ingestion
│   ├── silver_transformation.py # Data quality & cleansing
│   └── gold_aggregation.py      # Business-level aggregations
├── resources/
│   └── jobs/
│       └── medallion_job.yml    # Databricks job definition
├── tests/
│   ├── unit/                    # Unit tests (required)
│   └── integration/             # Integration tests
├── databricks.yml               # Bundle config (prod only)
└── README.md
```

---

## 🚀 **Workflow**

### **1. Create Feature Branch**
```bash
git checkout main
git pull origin main
git checkout -b feature/short-description
```

### **2. Make Changes (Keep Small!)**
- Edit notebooks, add tests
- Commit frequently with clear messages
- **Keep scope small** - aim to merge within 1-2 days

### **3. Push and Create PR**
```bash
git add .
git commit -m "Add customer validation logic"
git push origin feature/short-description
```

Create PR to `main` on GitHub.

### **4. CI Runs Automatically**
On PR creation, GitHub Actions runs:
- ✅ Code formatting (black)
- ✅ Linting (flake8)
- ✅ Unit tests (pytest)
- ✅ Integration tests
- ✅ Bundle validation

### **5. Review & Merge**
- Get PR approved by team
- **Merge to main** (squash merge recommended)

### **6. Auto-Deploy to Production**
On merge to main:
- ✅ Deploy bundle to Databricks
- ✅ Run medallion ETL job
- ✅ Create production tag
- 📧 Email notification on success/failure

---

## 🎯 **Environments**

Unlike GitFlow, trunk-based has **ONE environment**:

| Environment | Catalog | Schema | Branch | Deploy Trigger |
|-------------|---------|--------|--------|----------------|
| **PROD** | `trunk_based` | `trunk_based_prod` | `main` | Every merge to main |

### **How to Handle Incomplete Features?**

Use **feature flags** in your code:

```python
# In notebook
ENABLE_NEW_VALIDATION = dbutils.widgets.get("enable_new_validation") == "true"

if ENABLE_NEW_VALIDATION:
    # New feature code (not ready for all users)
    df = df.filter(col("email").isNotNull())
```

Or use Unity Catalog tags to control which data the feature processes.

---

## ✅ **CI/CD Pipeline**

### **On Pull Request to Main:**
```yaml
Jobs:
  validate:
    - Code formatting check
    - Linting
    - Unit tests (required - fails if missing)
    - Integration tests
    - Bundle validation
```

### **On Merge to Main:**
```yaml
Jobs:
  deploy-prod:
    - Deploy to production
    - Run ETL pipeline
    - Tag release
    - Email notification
```

---

## 🧪 **Testing Requirements**

Trunk-based development requires **high test coverage** because every merge goes to production:

- ✅ **Unit tests are mandatory** (CI fails without them)
- ✅ **Tests must pass** before merge
- ✅ **Integration tests recommended**
- ✅ **Code coverage should be > 80%**

Run tests locally:
```bash
# Unit tests
pytest tests/unit/ -v

# All tests
pytest tests/ -v

# With coverage
pytest --cov=notebooks --cov-report=term
```

---

## 📊 **Unity Catalog Setup**

### **Create Catalog & Schema:**
```sql
-- Run once in Databricks SQL
CREATE CATALOG IF NOT EXISTS trunk_based;
CREATE SCHEMA IF NOT EXISTS trunk_based.trunk_based_prod;

-- Grant permissions
GRANT USE CATALOG ON CATALOG trunk_based TO `mybeats320@gmail.com`;
GRANT USE SCHEMA ON SCHEMA trunk_based.trunk_based_prod TO `mybeats320@gmail.com`;
GRANT CREATE TABLE ON SCHEMA trunk_based.trunk_based_prod TO `mybeats320@gmail.com`;
```

---

## 🔧 **Setup Instructions**

### **1. GitHub Repository Setup**

1. **Create new repo** or use existing
2. **Set main as default branch**
3. **Add branch protection**:
   - Go to Settings → Branches → Add rule
   - Branch name: `main`
   - ✅ Require pull request reviews (1 approver)
   - ✅ Require status checks (validate job)
   - ✅ Require branches to be up to date
   - ❌ Do NOT allow direct pushes to main

4. **Add secret**:
   - Go to Settings → Secrets → New repository secret
   - Name: `DATABRICKS_TOKEN`
   - Value: Your Databricks personal access token

### **2. Local Setup**

```bash
# Clone repo
git clone <your-repo-url>
cd databricks-trunk-based

# Install Databricks CLI
curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh

# Authenticate
databricks configure --host https://dbc-68f6c19e-2b48.cloud.databricks.com

# Validate bundle
databricks bundle validate --target prod
```

### **3. Test CI/CD**

```bash
# Create test feature branch
git checkout -b feature/test-ci

# Make a small change
echo "# Test" >> README.md

# Push and create PR
git add .
git commit -m "Test CI pipeline"
git push origin feature/test-ci
```

Go to GitHub and create PR to `main`. Watch CI run!

---

## 🚨 **Important Reminders**

### **⚠️ Every Merge Goes to Production!**
- Make sure your feature is **complete** before merging
- Tests must **pass** (no exceptions)
- Get code **reviewed** by at least one person
- Keep changes **small** (easier to review and rollback)

### **🔄 Keep Feature Branches Short-Lived**
- Merge within **1-2 days** maximum
- If taking longer, break into smaller PRs
- Rebase frequently to stay up-to-date with main

### **🧪 High Test Coverage is Critical**
- Add tests for every feature
- No merge without tests
- Aim for > 80% coverage

---

## 🆘 **Rollback Procedure**

If a production deployment fails:

```bash
# Find the last working tag
git tag --sort=-creatordate | head -5

# Rollback to previous tag
git checkout prod-20260112-123456-42
git push origin main --force

# This triggers a new deployment with the old code
```

---

## 📈 **Best Practices**

1. **Commit Often** - Small, atomic commits
2. **Pull Frequently** - Stay synced with main
3. **Test Locally** - Run tests before pushing
4. **Small PRs** - Easier to review, faster to merge
5. **Feature Flags** - For incomplete features
6. **Monitor Production** - Watch dashboards after deploy
7. **Fast Rollback** - Be ready to revert if needed

---

## 🔗 **Resources**

- [Trunk-Based Development](https://trunkbaseddevelopment.com/)
- [Databricks Bundles Documentation](https://docs.databricks.com/en/dev-tools/bundles/)
- [GitHub Actions](https://docs.github.com/en/actions)

---

## 📞 **Contact**

For questions or issues, contact: mybeats320@gmail.com
