namespace MongoDB.Data.Interfaces
{
    public interface IDelete<T>
    {
        bool Delete(T id);
    }
}
