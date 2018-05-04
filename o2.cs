// C# example, violation of Open-Closed Principle
public class HumanResourceDepartment
{
    private IList<Engineer> _hiredEngineers;
    private IList<Manager> _hiredManagers;
    // if another character is added, this is not working.
    // You can use an interface and have a bunch of subclasses.
    // Substitute principle, Interface segregation

    public void Hire(Engineer engineer){
        engineer.SignContract();
        _hiredEngineers.Add(engineer);
    }

    public void Hire(Manager manager){
        manager.SignContract();
        _hiredManagers.Add(manager);
    }
}

// What about architects? etc..

// public class HumanResourceDepartment
// {
//     private IList<IEmployee> _employees;
//     public void Hire(IEmployee employee)
//     {
//         employee.SignContract();
//         _employees.Add(employee);
//     }
// }
