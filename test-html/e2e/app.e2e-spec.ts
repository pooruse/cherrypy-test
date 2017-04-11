import { TestHtmlPage } from './app.po';

describe('test-html App', () => {
  let page: TestHtmlPage;

  beforeEach(() => {
    page = new TestHtmlPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
