using System.Collections.Generic;

namespace dotNetCoremysql.Data.Interfaces
{
    public interface IGetAll<T> where T : class
    {
        IEnumerable<T> GetAll();
    }
}
