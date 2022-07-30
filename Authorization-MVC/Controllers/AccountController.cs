using System.Web.Mvc;
using AuthMVC.Models;
using AuthMVC.ViewModels;
using AuthMVC.Security;

namespace AuthMVC.Controllers
{
    public class AccountController : Controller
    {
        // GET: Account
        public ActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Login(AccountViewModel avm)
        {
            AccountModel am = new AccountModel();
            if (string.IsNullOrEmpty(avm.Account.UserName) ||
                string.IsNullOrEmpty(avm.Account.Password) ||
                am.login(avm.Account.UserName, avm.Account.Password) == null)
            {
                ViewBag.Error = "Login failed.";
                return View("Index");
            }
            SessionPersister.Username = avm.Account.UserName;
            return View("Success");
        }

        public ActionResult Logout()
        {
            SessionPersister.Username = string.Empty;
            return RedirectToAction("Index");
        }

    }
}